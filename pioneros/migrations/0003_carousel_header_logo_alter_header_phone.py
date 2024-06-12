# Generated by Django 5.0.6 on 2024-06-11 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pioneros', '0002_header_headersocial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('image', models.ImageField(upload_to='images/carousels/')),
            ],
        ),
        migrations.AddField(
            model_name='header',
            name='logo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/headerlogo/'),
        ),
        migrations.AlterField(
            model_name='header',
            name='phone',
            field=models.CharField(max_length=30),
        ),
    ]
