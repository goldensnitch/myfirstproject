# Generated by Django 2.2.10 on 2020-07-07 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0004_auto_20200707_0631'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='timesheet',
            unique_together={('Associate', 'Date')},
        ),
        migrations.AlterIndexTogether(
            name='timesheet',
            index_together={('Associate', 'Date')},
        ),
        migrations.RemoveField(
            model_name='timesheet',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='timesheet',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='timesheet',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='timesheet',
            name='updated_by',
        ),
    ]
