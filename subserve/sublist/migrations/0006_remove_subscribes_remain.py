# Generated by Django 2.1.1 on 2020-10-25 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sublist', '0005_auto_20201023_1544'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscribes',
            name='remain',
        ),
    ]
