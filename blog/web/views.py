from django.shortcuts import render
from ..models import Post

def posts_render(request): 
    #posteos = Post.objects.all()
    posteos = Post.objects.filter(published=True)
    return render(request, 'posts.html', {'posteos': posteos})

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post_detail.html', {'poster': post})
