from django.db import models
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    keyword = models.CharField(max_length= 50)

class shoe_info(models.Model):
    title = models.CharField(max_length = 100)
    model_name = models.CharField(max_length=50)
    model_image = models.CharField(max_length=300)
    price = models.IntegerField(default=0)
    brand = models.CharField(max_length= 50)
    link = models.CharField(max_length= 300)
    search_site = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.title
    

class datecom_shoe(models.Model):
    title = models.CharField(max_length = 100)
    model_number = models.CharField(max_length=50)
    model_image = models.CharField(max_length=300)
    link = models.CharField(max_length= 300)
    brand = models.CharField(max_length= 50)
    price = models.IntegerField(default=0)
    search_site = models.CharField(max_length = 50)
    date = models.DateField(("date"))
    bookmark = models.ManyToManyField(MyUser,related_name='bookmark_post')#다음 모델에 두가지의 속성값을 추가하겠다.

    def __str__(self):
        return self.title


class bookmark_list(models.Model):
    datecom_shoe = models.ForeignKey(datecom_shoe, on_delete = models.CASCADE, null = True)
    user = models.ForeignKey(MyUser, on_delete = models.CASCADE, null = True)



