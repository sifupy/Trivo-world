# Generated by Django 4.2.6 on 2023-11-06 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weddad', '0025_day_planner_n'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
    ]
