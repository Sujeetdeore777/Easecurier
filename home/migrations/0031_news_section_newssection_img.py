# Generated by Django 4.2.6 on 2023-10-11 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_trustedbuisness_heading_trustedbuisness_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='News_section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=2000)),
                ('buttontext', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Newssection_img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='myimage')),
            ],
        ),
    ]