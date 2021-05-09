# Generated by Django 3.2 on 2021-05-09 05:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0007_products_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acc', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Account', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
