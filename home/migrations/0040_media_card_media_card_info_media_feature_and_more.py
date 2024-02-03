# Generated by Django 4.2.6 on 2023-10-13 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0039_glosary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media_card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='myimage')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('button_url', models.CharField(max_length=500)),
                ('button_text', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Media_card_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Media_feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='myimage')),
                ('title', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Media_feature_card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='myimage')),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('button_url', models.CharField(max_length=500)),
                ('button_text', models.CharField(max_length=500)),
            ],
        ),
    ]
