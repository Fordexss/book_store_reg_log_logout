# Generated by Django 5.0.6 on 2024-07-12 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_category_book'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
