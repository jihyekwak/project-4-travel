# Generated by Django 4.0.4 on 2022-04-12 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_customuser_profile_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='continent',
            field=models.CharField(choices=[('North America', 'North America'), ('Europe', 'Europe'), ('Antarctica', 'Antarctica'), ('Asia', 'Asia'), ('Oceania', 'Oceania'), ('Sourth America', 'South America'), ('Africa', 'Africa')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='list',
            name='category',
            field=models.CharField(choices=[('To Do List', 'To Do List'), ('To Confrim List', 'To Do List'), ('Packing List', 'Packing List')], max_length=20),
        ),
        migrations.AlterField(
            model_name='list',
            name='priority',
            field=models.CharField(blank=True, choices=[('High', 'High'), ('Low', 'Low'), ('Medium', 'Medium'), ('None', 'None')], max_length=20),
        ),
    ]
