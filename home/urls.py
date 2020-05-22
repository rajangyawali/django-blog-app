from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.posts, name='posts'),
    path('blogs/<int:id>/', views.details, name='blog-details'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about')
]