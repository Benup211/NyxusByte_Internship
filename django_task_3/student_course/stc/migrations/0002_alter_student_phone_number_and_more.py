# Generated by Django 5.0 on 2023-12-14 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]
