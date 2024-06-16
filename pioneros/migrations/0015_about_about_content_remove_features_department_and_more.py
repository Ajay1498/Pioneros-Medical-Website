# Generated by Django 5.0.6 on 2024-06-16 04:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pioneros', '0014_subscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='About_Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='features',
            name='department',
        ),
        migrations.RemoveField(
            model_name='features',
            name='name',
        ),
        migrations.AddField(
            model_name='features',
            name='description',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='features',
            name='title',
            field=models.CharField(default=None, max_length=25),
        ),
        migrations.CreateModel(
            name='Features_Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pioneros.department')),
            ],
        ),
    ]
