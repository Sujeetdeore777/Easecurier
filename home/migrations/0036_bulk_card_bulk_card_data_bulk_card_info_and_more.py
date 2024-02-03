# Generated by Django 4.2.6 on 2023-10-12 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_hyperlocal_card_hyperlocal_card_info_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bulk_card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_image', models.ImageField(upload_to='myimage')),
                ('card_title', models.CharField(max_length=500)),
                ('card_description', models.TextField(blank=True, max_length=5000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bulk_card_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='myimage')),
            ],
        ),
        migrations.CreateModel(
            name='Bulk_card_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField(blank=True, max_length=5000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bulk_card_information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField(blank=True, max_length=5000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bulk_company_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField(blank=True, max_length=5000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bulk_company_logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='myimage')),
            ],
        ),
        migrations.CreateModel(
            name='Bulk_company_slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_slider', models.ImageField(upload_to='myimage')),
            ],
        ),
        migrations.CreateModel(
            name='Bulk_end',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('button_text', models.CharField(max_length=500)),
                ('button_url', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Bulk_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('card_image', models.ImageField(upload_to='myimage')),
            ],
        ),
        migrations.CreateModel(
            name='Bulk_info1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField(blank=True, max_length=5000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bulk_review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Bulk_review_card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_image', models.ImageField(upload_to='myimage')),
                ('card_title', models.CharField(max_length=500)),
                ('card_description', models.TextField(blank=True, max_length=5000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bulk_service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField(blank=True, max_length=5000, null=True)),
                ('button_text', models.CharField(max_length=500)),
                ('button_url', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='myimage')),
            ],
        ),
        migrations.CreateModel(
            name='Bulk_service_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField(blank=True, max_length=5000, null=True)),
                ('button_text', models.CharField(max_length=500)),
                ('button_url', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Bulk_slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Bulk_Suggetion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField(blank=True, max_length=5000, null=True)),
                ('image', models.ImageField(upload_to='myimage')),
            ],
        ),
        migrations.CreateModel(
            name='Bulk_Suggetion_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('button_text', models.CharField(max_length=500)),
                ('button_url', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Bulk_testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='myimage')),
                ('description', models.TextField(blank=True, max_length=5000, null=True)),
            ],
        ),
    ]