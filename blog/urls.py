from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('blogpost', views.PostList.as_view(), name='blog_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]