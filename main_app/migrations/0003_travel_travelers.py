# Generated by Django 4.0.3 on 2022-04-02 21:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0002_destination_alter_itinerary_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='travel',
            name='travelers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
