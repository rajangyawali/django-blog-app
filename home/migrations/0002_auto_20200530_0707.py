# Generated by Django 2.2 on 2020-05-30 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]