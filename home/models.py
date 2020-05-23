from django.db import models
from django.utils.text import slugify


# Create your models here.
CATEGORY_OPTIONS = (
    ('Technology', 'Technology'),
    ('Health', 'Health'),
    ('International', 'International'),
    ('Politics', 'Politics'),
    ('Society', 'Society'),
    ('Economics', 'Economics'),
    ('Education', 'Education'),
    ('Tourism', 'Tourism'),
    ('Development', 'Development'),
    ('Food', 'Food'),
    ('Fashion', 'Fashion'),
    ('Entertainment', 'Entertainment')
)


class Author(models.Model):
    first_name = models.CharField(max_length=20, verbose_name = 'First Name')
    last_name = models.CharField(max_length=20, verbose_name = 'Last Name')
    age = models.IntegerField()
    email = models.EmailField(max_length=30, unique=True, verbose_name= 'Email Address')
    phone = models.IntegerField(max_length=10)
    image= models.ImageField(upload_to='authorImages/', blank=True, null =True)


    def __str__(self):
        return self.first_name + ' ' + self.last_name

class BlogPost(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='blogImages/', blank=True, null=True)
    posted = models.DateTimeField(auto_now_add=True, verbose_name='Posted On')
    category = models.CharField(max_length= 20, choices=CATEGORY_OPTIONS)
    author = models.ForeignKey(Author, default=1, null=1, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = "Blog Posts"
        ordering = ['-posted']

    def __str__(self):
        return self.title

    def __save__(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

