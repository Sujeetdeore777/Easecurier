# Generated by Django 4.2.6 on 2023-10-10 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_slidermaincart2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brandtext',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=2000)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
    ]
