# Generated by Django 4.2.6 on 2023-10-10 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_featurecard'),
    ]

    operations = [
        migrations.CreateModel(
            name='Featurecard2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='myimage')),
                ('heading', models.CharField(max_length=2000)),
                ('description', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='featureheading2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=2000)),
                ('description', models.CharField(max_length=5000)),
            ],
        ),
    ]
