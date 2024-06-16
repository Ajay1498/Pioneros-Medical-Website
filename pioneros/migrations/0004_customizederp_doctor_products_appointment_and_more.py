# Generated by Django 5.0.6 on 2024-06-11 12:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pioneros', '0003_carousel_header_logo_alter_header_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomizedERP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('department', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images/products/')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=30)),
                ('from_date', models.CharField(max_length=50)),
                ('to_date', models.CharField(max_length=50)),
                ('problems', models.TextField(max_length=255)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pioneros.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='SocialMediaLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=50)),
                ('url', models.URLField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='urls', to='pioneros.doctor')),
            ],
        ),
    ]
