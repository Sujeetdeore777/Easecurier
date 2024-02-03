# Generated by Django 4.2.6 on 2023-10-10 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_suggested'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsheading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=2000)),
                ('buttontext', models.CharField(max_length=2000)),
                ('buttonurl', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Newsimg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='myimage')),
            ],
        ),
        migrations.CreateModel(
            name='Suggestedheading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=2000)),
            ],
        ),
    ]
