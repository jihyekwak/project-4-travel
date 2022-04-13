# Generated by Django 4.0.4 on 2022-04-13 02:04

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('travel_bucket_list', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=250), blank=True, null=True, size=None)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('continent', models.CharField(choices=[('Africa', 'Africa'), ('Antarctica', 'Antarctica'), ('Oceania', 'Oceania'), ('North America', 'North America'), ('Asia', 'Asia'), ('Europe', 'Europe'), ('Sourth America', 'South America')], max_length=50, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='destination_images/')),
                ('description', models.TextField()),
                ('things_to_do', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=250), blank=True, size=None)),
            ],
            options={
                'ordering': ['country'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='travel_images/')),
                ('departure_date', models.DateField()),
                ('return_date', models.DateField()),
                ('things_to_do', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=250), blank=True, null=True, size=None)),
                ('budget', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('destinations', models.ManyToManyField(blank=True, to='main_app.destination')),
                ('tags', models.ManyToManyField(to='main_app.tag')),
                ('travelers', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['departure_date'],
            },
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('To Confirm List', 'To Confirm List'), ('Packing List', 'Packing List'), ('To Do List', 'To Do List')], max_length=20)),
                ('item', models.CharField(max_length=250)),
                ('priority', models.CharField(blank=True, choices=[('None', 'None'), ('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], max_length=20)),
                ('is_completed', models.BooleanField(default=False)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('travel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lists', to='main_app.travel')),
            ],
            options={
                'ordering': ['category', 'is_completed'],
            },
        ),
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField()),
                ('date', models.DateField()),
                ('transportation', models.CharField(max_length=250)),
                ('accomodation', models.CharField(max_length=250)),
                ('things_to_do', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=250), size=None)),
                ('meals', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), size=None)),
                ('daily_budget', models.IntegerField(default=0)),
                ('destination', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='itineraries', to='main_app.destination')),
                ('travel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itineraries', to='main_app.travel')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('travel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main_app.travel')),
            ],
        ),
    ]
