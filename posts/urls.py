from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:id>/likes/', views.likes, name='likes'),
    
    path('<int:post_id>/comments/create/', views.comment_create, name='comment_create'),
    path('<int:post_id>/comments/<int:id>/delete/', views.comment_delete, name='comment_delete'),
    path('<int:id>/likes_async/', views.likes_async, name='likes_async'),
    
]