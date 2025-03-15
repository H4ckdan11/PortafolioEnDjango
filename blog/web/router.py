from django.urls import path
from .views import posts_render, post_detail

app_name = 'blog'

urlpatterns = [
    path('', posts_render, name='posts'),
    path('post/<int:id>/', post_detail, name='post'),
]