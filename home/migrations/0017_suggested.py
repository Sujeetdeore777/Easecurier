# Generated by Django 4.2.6 on 2023-10-10 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_brandimg2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggested',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='myimage')),
                ('heading', models.CharField(max_length=2000)),
                ('description', models.CharField(max_length=1000)),
                ('buttonname', models.CharField(max_length=1000)),
                ('buttonurl', models.CharField(max_length=1000)),
            ],
        ),
    ]
