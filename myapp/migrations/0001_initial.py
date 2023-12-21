# Generated by Django 4.2.6 on 2023-11-30 13:09

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
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.CharField(max_length=200)),
                ('resume', models.FileField(blank=True, null=True, upload_to='resume')),
                ('skill', models.CharField(max_length=200)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], default='male', max_length=200)),
                ('experinces', models.PositiveIntegerField(default=0)),
                ('address', models.CharField(max_length=200)),
                ('ph', models.CharField(max_length=200)),
                ('profil_pic', models.ImageField(blank=True, null=True, upload_to='profilepics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('salary', models.PositiveIntegerField()),
                ('experiences', models.PositiveIntegerField(default=0)),
                ('last_date', models.DateField()),
                ('vaccancies', models.PositiveIntegerField(default=1)),
                ('poster', models.ImageField(blank=True, null=True, upload_to='posterimage')),
                ('contact', models.CharField(max_length=200)),
                ('qualification', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applied_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'pendeing'), ('rejected', 'rejected'), ('pending', 'pendeing')], default='pending', max_length=200)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.jobs')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
