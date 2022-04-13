# Generated by Django 4.0.4 on 2022-04-13 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_alter_destination_continent_alter_list_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='continent',
            field=models.CharField(choices=[('Africa', 'Africa'), ('Sourth America', 'South America'), ('Europe', 'Europe'), ('North America', 'North America'), ('Antarctica', 'Antarctica'), ('Asia', 'Asia'), ('Oceania', 'Oceania')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='list',
            name='priority',
            field=models.CharField(blank=True, choices=[('Medium', 'Medium'), ('Low', 'Low'), ('None', 'None'), ('High', 'High')], max_length=20),
        ),
    ]
