# Generated by Django 2.2.10 on 2020-12-02 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0009_blogcomment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('completed', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
    ]
