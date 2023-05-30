from django.urls import path
from . import views
# from .views import register, user_login

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login')
]
