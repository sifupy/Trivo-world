# Generated by Django 4.2.5 on 2023-09-28 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weddad', '0002_remove_post_photo_post_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='published_time',
        ),
    ]
