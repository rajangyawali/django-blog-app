from django.shortcuts import render, get_object_or_404
from . models import BlogPost

categories = {'Technology' :1, 'Politics' : 2, 'Society' : 3, 'Economics' : 4, 'Education' : 1, 'Tourism' : 2,
                'Development' : 3,'Food' : 4, 'Fashion' : 1, 'Health' : 2, 'Entertainment' : 3, 'International' : 4}

count_val = zip([],[],[])

def home(request):
    posts = BlogPost.objects.all()
    post_categories = [post.category for post in posts]
    colors = [categories[category] for category in post_categories]      
    
    hero_posts = zip(posts[0:2], colors[0:2])    
    recent_posts = zip(posts[2:8], colors[2:8])
    sub_hero_posts = zip(posts[8:9], colors[8:9])
    sub_posts = zip(posts[9:15], colors[9:15])
 
    categories_count = [post_categories.count(key) for key in categories.keys()]
    categories_colors_counts = zip(categories.keys(), categories.values(), categories_count)

    context = {
        'hero_posts':hero_posts,
        'recent_posts':recent_posts,
        'sub_hero_posts':sub_hero_posts,
        'sub_posts':sub_posts,
        'categories_colors_counts':categories_colors_counts
    }
    return render(request, 'home/index.html', context)


def details(request, id):
    posts = BlogPost.objects.all()
    post_categories = [post.category for post in posts]
    categories_count = [post_categories.count(key) for key in categories.keys()] 
    categories_colors_counts = zip(categories.keys(), categories.values(), categories_count)
    
    post = get_object_or_404(BlogPost, id = id)
    context={
        'post':post,
        'categories_colors_counts':categories_colors_counts
        }
    return render (request, 'home/post-details.html', context)


def posts(request):
    posts = BlogPost.objects.all()
    post_categories = [post.category for post in posts]
    colors = [categories[category] for category in post_categories]
    posts = zip(posts, colors)

    categories_count = [post_categories.count(key) for key in categories.keys()] 
    categories_colors_counts = zip(categories.keys(), categories.values(), categories_count)
    
    context = {
        'posts':posts,
        'categories_colors_counts':categories_colors_counts
    }
    return render(request, 'home/posts.html', context)

def contact(request):
    news = BlogPost.objects.all()
    context ={'news':news}
    return render(request, 'home/contact.html', context)

def about(request):
    context ={}
    return render(request, 'home/contact.html', context)

def category(request):
    posts = BlogPost.objects.all()
    post_categories = [post.category for post in posts]

    colors = [categories[category] for category in post_categories]
    categories_count = [post_categories.count(key) for key in categories.keys()]    
 
    categories_colors_counts = zip(categories.keys(), categories.values(), categories_count)

    context = {
        'categories_colors_counts':categories_colors_counts
    }
    return render(request, 'home/categories.html', context)

def test(request):
    posts = BlogPost.objects.all()
    return render(request, 'home/test.html', {'posts':posts})