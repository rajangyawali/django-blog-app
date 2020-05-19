from django.db import models


# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=20, verbose_name = 'First Name')
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField(max_length=30, unique=True, verbose_name= 'Email Address')
    phone = models.IntegerField(max_length=10)


    def __str__(self):
        return self.first_name + ' ' + self.email

class BlogPost(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    image_field = models.ImageField(upload_to='blogImages/', blank=True, null=True)
    posted_on = models.DateTimeField(auto_now_add=True, verbose_name='Posted On')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

