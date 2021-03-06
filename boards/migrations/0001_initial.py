# Generated by Django 2.0.6 on 2019-05-24 06:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Associate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=50)),
                ('Last_Name', models.CharField(max_length=50)),
                ('Date_of_Birth', models.DateField()),
                ('FatherName', models.CharField(blank=True, max_length=100, verbose_name="Father's Name")),
                ('MotherName', models.CharField(blank=True, max_length=100, verbose_name="Mother's Name")),
                ('Address_Line_1', models.CharField(blank=True, max_length=255)),
                ('Address_Line_2', models.CharField(blank=True, max_length=255)),
                ('City', models.CharField(choices=[('Guwahati', 'Guwahati'), ('Chennai', 'Chennai')], default='Chennai', max_length=50)),
                ('State', models.CharField(choices=[('Assam', 'Assam'), ('Tamil Nadu', 'Tamil Nadu')], default='Tamil Nadu', max_length=50)),
                ('Pin_Code', models.CharField(blank=True, max_length=6)),
                ('PF', models.CharField(blank=True, max_length=20)),
                ('ESI', models.CharField(blank=True, max_length=20)),
                ('PAN', models.CharField(blank=True, max_length=10)),
                ('Aadhar', models.CharField(blank=True, max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Associates', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255, unique=True)),
                ('Address_Line_1', models.CharField(blank=True, max_length=255)),
                ('Address_Line_2', models.CharField(blank=True, max_length=255)),
                ('City', models.CharField(choices=[('Guwahati', 'Guwahati'), ('Chennai', 'Chennai')], default='Chennai', max_length=50)),
                ('State', models.CharField(choices=[('Assam', 'Assam'), ('Tamil Nadu', 'Tamil Nadu')], default='Tamil Nadu', max_length=50)),
                ('Pin_Code', models.CharField(blank=True, max_length=6)),
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
                ('Relationship', models.CharField(choices=[('Father', 'Father'), ('Mother', 'Mother'), ('Brother', 'Brother'), ('Sister', 'Sister')], default='Father', max_length=50)),
                ('Date_of_Birth', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('Associate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Dependants', to='boards.Associate')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Dependants', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=4000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='posts', to=settings.AUTH_USER_MODEL)),
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
                ('Quote_Date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('Client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Requests', to='boards.Client')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Requests', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='boards.Board')),
                ('starter', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='topics', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='boards.Topic'),
        ),
        migrations.AddField(
            model_name='post',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
