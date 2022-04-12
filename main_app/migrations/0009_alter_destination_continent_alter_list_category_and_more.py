# Generated by Django 4.0.4 on 2022-04-12 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_destination_continent_alter_list_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='continent',
            field=models.CharField(choices=[('Antarctica', 'Antarctica'), ('Europe', 'Europe'), ('North America', 'North America'), ('Oceania', 'Oceania'), ('Africa', 'Africa'), ('Sourth America', 'South America'), ('Asia', 'Asia')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='list',
            name='category',
            field=models.CharField(choices=[('Packing List', 'Packing List'), ('To Confrim List', 'To Do List'), ('To Do List', 'To Do List')], max_length=20),
        ),
        migrations.AlterField(
            model_name='list',
            name='priority',
            field=models.CharField(blank=True, choices=[('Medium', 'Medium'), ('High', 'High'), ('None', 'None'), ('Low', 'Low')], max_length=20),
        ),
    ]