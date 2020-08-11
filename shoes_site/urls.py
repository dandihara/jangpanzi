from django.urls import path
from shoes_site import views 
from .views import bookmark

#이곳의 규칙에 따라 페이지 주소가 형성되고 그에 따라 뷰의 형태가 달라짐.
urlpatterns = [
    path("", views.index, name = "index"),
    path("login/",views.login, name= "login"),
    path("sign_up/",views.sign_up, name= "sign_up"),
    path("logout/",views.logout, name= "logout"),
    path("search/",views.search),
    path("datecom/",views.datecom),
    path("howto/",views.howto),
    path("bookmark/<int:id>",bookmark.as_view(),name = 'bookmark'),
]