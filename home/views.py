from django.shortcuts import render
from . models import BlogPost
# from django.http import HttpResponse

def home(request):
    
    return render(request, 'home/index.html')


def posts(request):
    posts = BlogPost.objects.all()
    print(posts)
    context = {
        'posts':posts
    }

    return render(request, 'home/post.html', context)