# Generated by Django 2.2.10 on 2020-07-09 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0007_auto_20200709_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='Views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
