# Generated by Django 4.0.4 on 2022-04-13 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_alter_customuser_profile_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='continent',
            field=models.CharField(choices=[('Sourth America', 'South America'), ('Asia', 'Asia'), ('North America', 'North America'), ('Africa', 'Africa'), ('Oceania', 'Oceania'), ('Europe', 'Europe'), ('Antarctica', 'Antarctica')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='list',
            name='category',
            field=models.CharField(choices=[('To Confrim List', 'To Confrim List'), ('Packing List', 'Packing List'), ('To Do List', 'To Do List')], max_length=20),
        ),
        migrations.AlterField(
            model_name='list',
            name='priority',
            field=models.CharField(blank=True, choices=[('Medium', 'Medium'), ('Low', 'Low'), ('None', 'None'), ('High', 'High')], max_length=20),
        ),
    ]
