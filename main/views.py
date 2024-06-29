from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def index(request):
    post = Post.objects.get(id=1)
    context = {
        'post' : post,
    }
    return render(request, 'main/index.html', context)

def index(request):
    return render(request, 'main/index.html')

def post(request, post_id):
    return HttpResponse(f"Post ID {post_id}")

def all_posts(request):
    return HttpResponse("All Posts")

def category(request, cat_id):
    return HttpResponse(f"Category ID {cat_id}")

def all_categories(request):
    return HttpResponse("All Categories")