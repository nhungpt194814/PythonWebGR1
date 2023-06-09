from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog'),
    # blog/id: đây là hardcode url và cần được loại bỏ
    path('create_post', views.create_post, name='create_post'),
    path('<int:pk>/', views.post, name='post')
]
