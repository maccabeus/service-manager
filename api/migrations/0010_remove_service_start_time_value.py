# Generated by Django 3.2.4 on 2021-06-30 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_service_start_time_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='start_time_value',
        ),
    ]
