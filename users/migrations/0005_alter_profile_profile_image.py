# Generated by Django 4.2.3 on 2023-08-09 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_skill_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='profiles/user-default.png', null=True, upload_to='profiles/'),
        ),
    ]
