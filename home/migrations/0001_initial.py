# Generated by Django 2.2 on 2020-05-27 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Advertisement Name')),
                ('company', models.CharField(max_length=50, verbose_name='Advertisement Company')),
                ('type', models.CharField(choices=[('Main', 'Main'), ('Side', 'Side')], max_length=10)),
                ('image', models.ImageField(upload_to='advertisementImages')),
                ('posted', models.DateTimeField(auto_now_add=True, verbose_name='Posted On')),
            ],
            options={
                'verbose_name_plural': 'Advertisement Images',
                'ordering': ['-posted'],
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=20, verbose_name='Last Name')),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=30, unique=True, verbose_name='Email Address')),
                ('phone', models.IntegerField(max_length=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='authorImages/')),
                ('description', models.CharField(blank=True, max_length=100, null=True, verbose_name='Short Info')),
            ],
        ),
        migrations.CreateModel(
            name='AuthorFollowLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook_link', models.URLField(blank=True, null=True)),
                ('twitter_link', models.URLField(blank=True, null=True)),
                ('google_plus_link', models.URLField(blank=True, null=True)),
                ('instagram_link', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Authors Follow Link',
            },
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('featured', models.CharField(choices=[('True', 'True'), ('False', 'False')], default='False', max_length=5)),
                ('slug', models.SlugField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='blogImages/')),
                ('posted', models.DateTimeField(auto_now_add=True, verbose_name='Posted On')),
                ('category', models.CharField(choices=[('Technology', 'Technology'), ('Health', 'Health'), ('International', 'International'), ('Politics', 'Politics'), ('Society', 'Society'), ('Economics', 'Economics'), ('Education', 'Education'), ('Tourism', 'Tourism'), ('Development', 'Development'), ('Food', 'Food'), ('Fashion', 'Fashion'), ('Entertainment', 'Entertainment')], max_length=20)),
                ('author', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Author')),
            ],
            options={
                'verbose_name_plural': 'Blog Posts',
                'ordering': ['-posted'],
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email Address')),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Message from Customers',
            },
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=20, null=True)),
                ('search', models.CharField(max_length=256)),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Searched on')),
            ],
            options={
                'verbose_name_plural': 'Searches',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscriber', models.EmailField(max_length=30, unique=True, verbose_name='Subscriber Email')),
                ('subscribed', models.DateTimeField(auto_now_add=True, verbose_name='Sunscribed On')),
            ],
            options={
                'verbose_name_plural': 'Subscribers List',
                'ordering': ['-subscribed'],
            },
        ),
        migrations.CreateModel(
            name='PostImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='postImages/')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.BlogPost')),
            ],
            options={
                'verbose_name_plural': 'Post Images',
            },
        ),
        migrations.AddField(
            model_name='author',
            name='links',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.AuthorFollowLinks'),
        ),
    ]
