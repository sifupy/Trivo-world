# Generated by Django 4.2.5 on 2023-10-13 17:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('weddad', '0014_alter_plan_member_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan_member',
            name='member',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
