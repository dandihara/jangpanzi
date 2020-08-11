from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from shoes_site.models import shoe_info,datecom_shoe,MyUser
# Register your models here.
admin.site.register(shoe_info)
admin.site.register(datecom_shoe)
admin.site.register(MyUser,UserAdmin)