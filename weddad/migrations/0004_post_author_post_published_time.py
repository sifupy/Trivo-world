# Generated by Django 4.2.5 on 2023-09-29 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weddad', '0003_remove_post_published_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='published_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
