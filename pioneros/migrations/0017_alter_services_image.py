# Generated by Django 5.0.6 on 2024-06-24 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pioneros', '0016_services'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='image',
            field=models.ImageField(upload_to='images/services/'),
        ),
    ]