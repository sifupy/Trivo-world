# Generated by Django 4.2.5 on 2023-09-27 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weddad', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='photo',
        ),
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]
