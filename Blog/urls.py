from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('<int:post_id>/', views.blog_detail, name='blog_detail'),
    path('search/', views.blog_search, name='blog_search'),
    path('signup/', views.signup, name='signup'),
    path('create/', views.create_blog_post, name='create_blog_post'),
    path('<int:post_id>/edit/', views.edit_blog_post, name='edit_blog_post'),
    path('<int:post_id>/delete/', views.delete_blog_post, name='delete_blog_post'),
]
