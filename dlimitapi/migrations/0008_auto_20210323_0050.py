# Generated by Django 3.1.7 on 2021-03-23 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dlimitapi', '0007_auto_20210323_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(null=True),
        ),
    ]
