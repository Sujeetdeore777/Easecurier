# Generated by Django 4.2.6 on 2023-10-13 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0038_faq_card_faq_info_card_faq_page_faq_section_card'),
    ]

    operations = [
        migrations.CreateModel(
            name='Glosary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
