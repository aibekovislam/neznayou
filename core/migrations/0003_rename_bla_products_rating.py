# Generated by Django 3.2 on 2021-05-07 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_products_bla'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='bla',
            new_name='rating',
        ),
    ]
