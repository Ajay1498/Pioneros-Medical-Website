# Generated by Django 5.0.6 on 2024-06-11 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pioneros', '0005_department_appointment_title_alter_doctor_department_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='from_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='to_date',
            new_name='time',
        ),
    ]