# Generated by Django 4.2.3 on 2023-08-03 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_featured_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='featured_images',
        ),
        migrations.AddField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, default='img1.jpeg', null=True, upload_to=''),
        ),
    ]
