from django.contrib import admin
from .models import User
# Register your models here.
# show your users on admin site


class CustomUser(admin.ModelAdmin):
    list_display = ['username', 'email', 'full_name', 'address']
    search_fields = ['username', 'email']
    list_filter = ['username']


# admin.site.unregister(User)
admin.site.register(User, CustomUser)
