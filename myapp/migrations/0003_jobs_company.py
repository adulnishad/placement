# Generated by Django 4.2.7 on 2023-12-05 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_applications_projects_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='company',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
