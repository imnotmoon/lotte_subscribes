# Generated by Django 2.1.1 on 2020-10-19 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0009_auto_20200922_2326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='description',
        ),
    ]
