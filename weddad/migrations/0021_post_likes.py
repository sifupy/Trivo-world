# Generated by Django 4.2.6 on 2023-10-22 20:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('weddad', '0020_plan_member3_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='trip_post', to=settings.AUTH_USER_MODEL),
        ),
    ]
