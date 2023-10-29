# Generated by Django 4.2.5 on 2023-10-13 17:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('weddad', '0017_rename_plan_member_plan_member2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan_member3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('badge', models.CharField(blank=True, max_length=25, null=True)),
                ('status', models.CharField(blank=True, default='Non')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Plan_memberchip', to=settings.AUTH_USER_MODEL)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='weddad.plan')),
            ],
        ),
        migrations.DeleteModel(
            name='Plan_member2',
        ),
    ]