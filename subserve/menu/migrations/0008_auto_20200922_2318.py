# Generated by Django 2.1.1 on 2020-09-22 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_auto_20200922_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='store_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='store_id', to='store.Store'),
        ),
    ]
