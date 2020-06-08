from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Blog
# Create your views here.
def all_blogs(request):
    #blogs = Blog.objects.all()
    blogs = Blog.objects.order_by('-date')[:5] #it will come the lastest post by date and display only 5 posts
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})

def detail(request, blog_id):
    blogs = Blog.objects.order_by('-date')
    blog = get_object_or_404(Blog, pk = blog_id) #primary key
    return render(request, 'blog/detail.html', {'blog':blog, 'blogs':blogs})