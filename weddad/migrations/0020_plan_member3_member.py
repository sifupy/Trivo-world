# Generated by Django 4.2.5 on 2023-10-13 17:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('weddad', '0019_remove_plan_member3_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan_member3',
            name='member',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Plan_memberchip', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
