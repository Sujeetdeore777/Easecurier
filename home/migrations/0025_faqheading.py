# Generated by Django 4.2.6 on 2023-10-11 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_prisingcart2_prisingcart2heading'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faqheading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=2000)),
            ],
        ),
    ]
