from django.shortcuts import render,redirect,get_object_or_404
from .models import shoe_info,datecom_shoe,bookmark_list,MyUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from urllib.parse import urlparse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from django.views.generic.base import View
from django.db.models import Q
from datetime import datetime
from django.http import HttpResponseForbidden
import random

# Create your views here.
#사용자의 요청 받는 함수
def datecom(req):
    shoes_datecom = datecom_shoe.objects.all()
    template = 'datecom.html'
    context = {'datecom_shoes':shoes_datecom}
    return render(req,template,context)

def search(req):
    #shoes_info_search = shoes_info.filter(title__icontains = 'Air Max')검색방식
    #order_by('price')[:4] 순서도 - > 오름차순 none > 내림차순
    # {html한테 넘겨줄 이름 : 현재 이 함수내 이름}
    shoes_info = shoe_info.objects.all()
    try:
        q = req.GET.get('keyword')
    except:
        q = None
    if q:
        search_keyword = q
        if q =='에어맥스' or q == 'airmax': #검색어와 찾고자 하는 아이템 일치
            q = 'Air Max'
        elif q == 'm2k':
            q = 'M2K'
        elif q == '베이퍼맥스':
            q ='vapormax'
        elif q =='영원' or q == '영96':
            q = 'yung'
        elif q == '컨버스' or q == '척테일러':
            q = 'converse'
        elif q == '나이키':
            q = 'nike'
        elif q == '아디다스':
            q = 'adidas'
        shoes_info_search = shoes_info.filter(Q(title__icontains = q) | Q(brand__icontains = q)).order_by('price') #icontains = %q%
        templete = 'shoe_search.html'
        context = {'shoes_info':shoes_info_search, 'query': search_keyword}
    else:
        templete = 'shoe_search.html'
        context = {}
    return render(req, templete, context)

def index(req):
    result_recomm = []
    if req.user.is_authenticated:
        user = req.user
        keyword_string = user.keyword
        keyword_list = keyword_string.split(',')
        for keyword in keyword_list:
            if keyword == '나이키':
                keyword = 'nike'
            elif keyword == '아디다스':
                keyword = 'adidas'
            elif keyword == '컨버스':
                keyword = 'converse'
            elif keyword == '푸마':
                keyword = 'puma'
            elif keyword == '뉴발란스':
                keyword ='new balance'
            elif keyword == '아식스':
                keyword = 'asics'
            temp = shoe_info.objects.all()
            recomm = list(temp.filter(brand__icontains = keyword).order_by('?'))
            result_recomm = recomm + result_recomm
        results = user.bookmark_post.all()
        temp = shoe_info.objects.order_by('?')
        print(results)
        shoes_info = shoe_info.objects.order_by('?')[:4]
        random.shuffle(result_recomm)
        recomm_shoes = result_recomm[:12]
        datecom = datecom_shoe.objects.order_by('?')[:4]
        return render(req, "index.html",{'shoes_info':recomm_shoes,'datecom_shoes':datecom,'bookmark_list':results})
    else:
        shoes_info = shoe_info.objects.order_by('?')[:4]
        datecom = datecom_shoe.objects.order_by('?')[:4]
    return render(req, "index.html",{'shoes_info':shoes_info,'datecom_shoes':datecom})

def login(req):
    if req.method == 'POST':
        id = req.POST.get('id', '')
        pw = req.POST.get('pw', '')
        user = authenticate(username = id, password = pw)
        if user is not None:
            auth.login(req, user)
            return redirect('index')    
        else:#js 파일 만들어 넣기
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        return render(req, "login.html")

def logout(req):
    auth.logout(req)
    return redirect('index')

def sign_up(req):
    if req.method == "POST":
        if req.POST["pw"] == req.POST["pw_confirm"]:
            user = MyUser.objects.create_user(
                username = req.POST["id"],password= req.POST["pw"],keyword = req.POST["user_keyword"])
            auth.login(req,user)
            user.save()
            return redirect('index')
        else:
            return redirect('sign_up')
    else:
        return render(req,'sign_up.html')


class bookmark(View):
    def get(self, req, *args, **kwargs):
        if not req.user.is_authenticated: #login확인
            return redirect('login')
        else:
            print(kwargs)#kwargs = {'id': 2 } >>> datecom_shoe의 id
            print(req.user)
            if 'id' in kwargs:
                datecom_shoe_id = kwargs['id']
                shoe = datecom_shoe.objects.get(pk = datecom_shoe_id)
                user = req.user
                if user in shoe.bookmark.all():
                    shoe.bookmark.remove(user)
                else:
                    shoe.bookmark.add(user)

            referer_url = req.META.get('HTTP_REFERER')
            path = urlparse(referer_url).path
            return HttpResponseRedirect(path)


def howto(req):
    templete = 'howto.html'
    return render(req,templete)

