# Generated by Django 2.0.6 on 2018-07-12 09:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boards', '0003_associate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255, unique=True)),
                ('AddressLine1', models.CharField(blank=True, max_length=255)),
                ('AddressLine2', models.CharField(blank=True, max_length=255)),
                ('City', models.CharField(choices=[('Guwahati', 'Guwahati'), ('Chennai', 'Chennai')], default='Chennai', max_length=50)),
                ('State', models.CharField(choices=[('Assam', 'Assam'), ('Tamil Nadu', 'Tamil Nadu')], default='Tamil Nadu', max_length=50)),
                ('PinCode', models.CharField(blank=True, max_length=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Clients', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dependant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Relationship', models.CharField(choices=[('Father', 'Father'), ('Mother', 'Mother')], default='Father', max_length=50)),
                ('DateOfBirth', models.DateTimeField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('Associate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Dependants', to='boards.Associate')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Dependants', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Project', models.CharField(max_length=255)),
                ('Details', models.TextField(max_length=4000)),
                ('Type', models.CharField(choices=[('Ad-hoc', 'Ad-hoc'), ('Tender', 'Tender')], default='Ad-hoc', max_length=50)),
                ('Status', models.CharField(choices=[('New Request', 'New Request'), ('Quote In Progress', 'Quote In Progress'), ('Quote Sent', 'Quote Sent')], default='New', max_length=50)),
                ('QuoteDate', models.DateTimeField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('Client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Requests', to='boards.Client')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Requests', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
