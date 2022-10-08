from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from account.models import MyUser

class MyUserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None, {
                "classes": ("wide"),
                "fields"  : ("email", "full_name", "password1", "password2")
            }
        )
    )
admin.site.register(MyUser, MyUserAdmin)