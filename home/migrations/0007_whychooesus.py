# Generated by Django 4.2.6 on 2023-10-10 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_plan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Whychooesus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=2000)),
                ('description', models.CharField(max_length=5000)),
            ],
        ),
    ]
