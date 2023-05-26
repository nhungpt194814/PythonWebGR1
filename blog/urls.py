from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog'),
    # blog/id: đây là hardcode url và cần được loại bỏ

    path('<int:pk>/', views.post, name='post')
]
