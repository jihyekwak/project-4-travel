# Generated by Django 4.0.3 on 2022-04-01 22:53

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_itinerary'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itinerary',
            old_name='things_todo',
            new_name='things_to_do',
        ),
        migrations.AddField(
            model_name='itinerary',
            name='daily_budget',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='meals',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), size=None),
        ),
    ]