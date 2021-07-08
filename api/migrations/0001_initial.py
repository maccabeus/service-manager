# Generated by Django 3.2.5 on 2021-07-08 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('setting', models.CharField(help_text='Setting name', max_length=250)),
                ('value', models.CharField(help_text='value of the setting', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="The customer's name", max_length=250)),
                ('email', models.EmailField(help_text='user valid email address', max_length=100)),
                ('phone', models.CharField(help_text='user valid phone number', max_length=100)),
                ('date_created', models.DateField(auto_now_add=True, verbose_name="date customer's account was created")),
                ('time_created', models.TimeField(auto_now_add=True, verbose_name="time customer's account was created")),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name="date customer's account was created")),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="The staff's name", max_length=250)),
                ('email', models.EmailField(help_text='staff valid email address', max_length=100)),
                ('phone', models.CharField(help_text='staff valid phone number', max_length=100)),
                ('department', models.CharField(help_text='departmen of the staff', max_length=100)),
                ('date_created', models.DateField(auto_now_add=True, verbose_name="date staff's account was created")),
                ('time_created', models.TimeField(auto_now_add=True, verbose_name="time staff's account was created")),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name="date staff's account was created")),
            ],
        ),
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name=' holiday date when services cannot be booked')),
                ('description', models.TextField(help_text='Brief description about this holiday')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of this service', max_length=100)),
                ('description', models.CharField(help_text='The service description. What this service is all about', max_length=100)),
                ('duration', models.FloatField(verbose_name='The duration in minues required for task completion')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='date service is created')),
                ('time_created', models.TimeField(auto_now_add=True, verbose_name='time service is created')),
                ('updated_at', models.DateTimeField(null=True, verbose_name='date and time service is updated')),
            ],
        ),
        migrations.CreateModel(
            name='WorkOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_id', models.BigIntegerField(verbose_name='the service Id linked to this order')),
                ('employee_id', models.BigIntegerField(verbose_name='the emplyee Id assigned to treat this order')),
                ('description', models.TextField(help_text='The order descriptions')),
                ('customer_id', models.EmailField(default='', help_text="The customer's email address", max_length=100)),
                ('duration', models.FloatField(verbose_name='The duration in minues required for task completion')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='date order is created')),
                ('time_created', models.TimeField(auto_now_add=True, verbose_name='time order is created')),
                ('start_time', models.CharField(default=None, max_length=100, verbose_name='The actual time the order is scheduled to start')),
                ('end_time', models.CharField(default=None, max_length=100, verbose_name='The time the order is scheduled to end')),
                ('end_date', models.CharField(default=None, max_length=100, verbose_name='The date the service request ends')),
                ('start_time_value', models.FloatField(default=None, verbose_name='number representation of starr time')),
                ('end_time_value', models.FloatField(default=None, verbose_name='number representation of end time')),
                ('updated_at', models.DateTimeField(null=True, verbose_name='date and time order is updated')),
                ('done', models.BigIntegerField(default=0, verbose_name='Will be 1 when service request is done')),
                ('deleted', models.BigIntegerField(default=0, verbose_name='A field to track deleted request> this request will be available for audit purposes')),
            ],
        ),
        migrations.AddIndex(
            model_name='workorder',
            index=models.Index(fields=['date_created'], name='api_workord_date_cr_4d418a_idx'),
        ),
        migrations.AddIndex(
            model_name='workorder',
            index=models.Index(fields=['customer_id'], name='api_workord_custome_2f120d_idx'),
        ),
        migrations.AddIndex(
            model_name='workorder',
            index=models.Index(fields=['deleted'], name='api_workord_deleted_6d0c74_idx'),
        ),
        migrations.AddIndex(
            model_name='workorder',
            index=models.Index(fields=['done'], name='api_workord_done_44c828_idx'),
        ),
        migrations.AddIndex(
            model_name='workorder',
            index=models.Index(fields=['id'], name='api_workord_id_89db5c_idx'),
        ),
        migrations.AddIndex(
            model_name='workorder',
            index=models.Index(fields=['start_time_value'], name='api_workord_start_t_08ff94_idx'),
        ),
        migrations.AddIndex(
            model_name='workorder',
            index=models.Index(fields=['end_time_value'], name='api_workord_end_tim_191055_idx'),
        ),
        migrations.AddIndex(
            model_name='service',
            index=models.Index(fields=['date_created'], name='api_service_date_cr_35573f_idx'),
        ),
        migrations.AddIndex(
            model_name='service',
            index=models.Index(fields=['id'], name='api_service_id_2f1f59_idx'),
        ),
        migrations.AddIndex(
            model_name='holiday',
            index=models.Index(fields=['date'], name='api_holiday_date_1a4423_idx'),
        ),
        migrations.AddIndex(
            model_name='employee',
            index=models.Index(fields=['id'], name='api_employe_id_de9f32_idx'),
        ),
        migrations.AddIndex(
            model_name='customer',
            index=models.Index(fields=['date_created'], name='api_custome_date_cr_b4a3c3_idx'),
        ),
        migrations.AddIndex(
            model_name='customer',
            index=models.Index(fields=['id'], name='api_custome_id_2c695e_idx'),
        ),
        migrations.AddIndex(
            model_name='appsettings',
            index=models.Index(fields=['setting'], name='api_appsett_setting_203a94_idx'),
        ),
    ]
