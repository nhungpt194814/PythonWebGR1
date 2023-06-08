# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):
    list_display = ['email', 'first_name', 'last_name', 'address', 'is_staff']
    search_fields = ['first_name', 'email']
    ordering = ['first_name']


admin.site.register(User, UserAdmin)
# admin.site.register(User, CustomUserAdmin)
