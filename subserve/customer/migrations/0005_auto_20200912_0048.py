# Generated by Django 2.1.1 on 2020-09-12 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_auto_20200912_0008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='customer_id',
            new_name='id',
        ),
    ]