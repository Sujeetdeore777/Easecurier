# Generated by Django 4.2.6 on 2023-10-10 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_brandimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brandimg2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='myimage')),
            ],
        ),
    ]
