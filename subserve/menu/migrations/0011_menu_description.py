# Generated by Django 2.1.1 on 2020-10-19 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0010_remove_menu_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='description',
            field=models.CharField(default='', max_length=45),
        ),
    ]