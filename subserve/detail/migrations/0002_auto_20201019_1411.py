# Generated by Django 2.1.1 on 2020-10-19 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='address',
            field=models.CharField(default='주소없음', max_length=45, null=True),
        ),
    ]
