# Generated by Django 3.2 on 2021-05-08 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_products_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='is_active',
        ),
    ]
