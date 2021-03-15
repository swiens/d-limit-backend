# Generated by Django 3.1.7 on 2021-03-15 20:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Drinker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField(max_length=55)),
                ('age', models.IntegerField(max_length=55)),
                ('weight', models.IntegerField(max_length=55)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('drinker_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dlimitapi.drinker')),
            ],
        ),
        migrations.CreateModel(
            name='EventDrink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_drank', models.TimeField()),
                ('drink_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dlimitapi.drink')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dlimitapi.event')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('phone', phone_field.models.PhoneField(max_length=31, unique=True)),
                ('drinker_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dlimitapi.drinker')),
            ],
        ),
    ]
