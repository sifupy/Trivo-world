# Generated by Django 4.2.6 on 2023-11-01 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weddad', '0024_alter_plan_food_costs_alter_plan_other_costs_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='day_planner',
            name='n',
            field=models.IntegerField(default=0),
        ),
    ]
