# Generated by Django 4.2.6 on 2023-10-10 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_subimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buisness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smallheading', models.CharField(max_length=2000)),
                ('heading', models.CharField(max_length=2000)),
                ('description', models.CharField(max_length=2000)),
            ],
        ),
    ]
