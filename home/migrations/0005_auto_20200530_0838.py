# Generated by Django 2.2 on 2020-05-30 02:53

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200530_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]