# Generated by Django 5.0 on 2023-12-18 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['created_at']},
        ),
    ]