from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    # path('', views.category, name='categories'),
    path('tests/', views.test, name='test'),
    path('posts/', views.posts, name='posts'),
    path('posts/<int:id>/', views.details, name='details'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about')
]