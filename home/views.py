from django.shortcuts import render
from . models import BlogPost

categories = {'Technology' :1, 'Politics' : 2, 'Society' : 3, 'Economics' : 4, 'Education' : 1, 'Tourism' : 2,
                'Development' : 3,'Food' : 4, 'Fashion' : 1, 'Health' : 2, 'Entertainment' : 3, 'International' : 4}

def home(request):
    posts = BlogPost.objects.all()
    colors = [post.category for post in posts]
    colors = [categories[color] for color in colors]
    
    hero_posts = zip(posts[0:2], colors[0:2])    
    recent_posts = zip(posts[2:8], colors[2:8])
    sub_hero_posts = zip(posts[8:9], colors[8:9])
    sub_posts = zip(posts[9:15], colors[9:15])
    context = {
        'hero_posts':hero_posts,
        'recent_posts':recent_posts,
        'sub_hero_posts':sub_hero_posts,
        'sub_posts':sub_posts,
    }
    return render(request, 'home/index.html', context)

def details(request, id):
    post = BlogPost.objects.get(id=id)
    context={
        'post':post
        }
    return render (request, 'home/blog-details.html', context)


def posts(request):
    posts = BlogPost.objects.all()
    print(posts)
    context = {
        'posts':posts
    }

    return render(request, 'home/post.html', context)

def contact(request):
    news = BlogPost.objects.all()
    context ={'news':news}
    return render(request, 'home/contact.html', context)

def about(request):
    context ={}
    return render(request, 'home/contact.html', context)