# Generated by Django 2.2.10 on 2020-07-09 14:46

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0006_blog_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='Details',
        ),
        migrations.AlterField(
            model_name='blog',
            name='Content',
            field=tinymce.models.HTMLField(verbose_name='Content'),
        ),
    ]
