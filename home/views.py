from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.db.models import Q
from . models import BlogPost, Search, Contact, Advertisement
from .forms import ContactForm
from django.contrib import messages

flag = 0
categories = {'Technology' :1, 'Politics' : 2, 'Society' : 3, 'Economics' : 4, 'Education' : 1, 'Tourism' : 2,
                'Development' : 3,'Food' : 4, 'Fashion' : 1, 'Health' : 2, 'Entertainment' : 3, 'International' : 4}

def main_adv():
    return Advertisement.objects.all().filter(type='Main')

def side_adv():
    return Advertisement.objects.all().filter(type='Side')    

def categories_counts(posts):
    post_categories = [post.category for post in posts]
    categories_count = [post_categories.count(key) for key in categories.keys()] 
    return zip(categories.keys(), categories.values(), categories_count)

def home(request):
    posts = BlogPost.objects.all()
    categories_colors_counts = categories_counts(posts)

    post_categories = [post.category for post in posts]
    colors = [categories[category] for category in post_categories]      
    
    hero_posts = zip(posts[0:2], colors[0:2])    
    recent_posts = zip(posts[2:8], colors[2:8])
    sub_hero_posts = zip(posts[8:9], colors[8:9])
    sub_posts = zip(posts[9:15], colors[9:15])

    context = {
        'hero_posts':hero_posts,
        'recent_posts':recent_posts,
        'sub_hero_posts':sub_hero_posts,
        'sub_posts':sub_posts,
        'categories_colors_counts':categories_colors_counts,
        'main_adv':main_adv(),
        'side_adv':side_adv()
    }
    return render(request, 'home/index.html', context)


def details(request, slug):
    global flag
    if flag == 0:    
        posts = BlogPost.objects.all()
        my_posts = posts
    else:
        posts = my_posts
        flag = 1
    print(flag)
    categories_colors_counts = categories_counts(posts)

    post = get_object_or_404(BlogPost, slug = slug)
    context={
        'post':post,
        'categories_colors_counts':categories_colors_counts,
        'main_adv':main_adv(),
        'side_adv':side_adv()
        }
    return render (request, 'home/post-details.html', context)


def posts(request, category):
    all_posts = BlogPost.objects.all()
    search_query = request.GET.get('q')
    search_message=''
    if search_query:
        posts = all_posts.filter(Q(title__icontains = search_query))
        search = Search(user=request.user, search=search_query)
        search.save()
        if not posts:
            search_message = '<i> No results found for your search query !! </i>'
    else:
        if category== 'posts':
            posts = all_posts
        else:
            posts = all_posts.filter(category = category)
    categories_colors_counts = categories_counts(all_posts)

    post_categories = [post.category for post in posts]
    colors = [categories[category] for category in post_categories]
    posts = zip(posts, colors) 
    context={
        'category':category,
        'posts':posts,
        'categories_colors_counts':categories_colors_counts,
        'search_message':search_message,
        'main_adv':main_adv(),
        'side_adv':side_adv()
    }
    return render(request, 'home/posts.html', context)

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']            
            message = form.cleaned_data['message']
            contact = Contact(email=email, subject=subject, message=message)
            contact.save()
            messages.success(request, 'Your message has been sent. Thank you !!')
            return redirect('home')
        else:
            messages.error(request, "Error sending message !")
            return render(request, "home/contact.html", context={"form":form})

    return render(request, 'home/contact.html', context={"form":form})

def about(request):
    context ={
        'main_adv':main_adv(),
        'side_adv':side_adv()
    }
    return render(request, 'home/about.html', context)

def searchPosts(request):
    search_query = request.GET.get('q')

# def category(request):
#     posts = BlogPost.objects.all()
#     post_categories = [post.category for post in posts]

#     colors = [categories[category] for category in post_categories]
#     categories_count = [post_categories.count(key) for key in categories.keys()]    
 
#     categories_colors_counts = zip(categories.keys(), categories.values(), categories_count)

#     context = {
#         'categories_colors_counts':categories_colors_counts
#     }
#     return render(request, 'home/categories.html', context)
    

def test(request):
    posts = BlogPost.objects.all()
    return render(request, 'home/test.html', {'posts':posts})

def error_404(request, exception):
    return render(request, 'home/error_404.html', status='404')

def error_500(request):
    return render(request, 'home/error_500.html', status='500')
