# Generated by Django 3.0.7 on 2020-06-18 15:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='produc_type',
            new_name='product_type',
        ),
        migrations.AddField(
            model_name='product',
            name='date_uploaded',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
