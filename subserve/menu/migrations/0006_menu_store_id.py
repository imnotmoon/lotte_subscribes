# Generated by Django 2.1.1 on 2020-09-22 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20200920_2215'),
        ('menu', '0005_remove_menu_store_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='store_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='store_id', to='store.Store'),
        ),
    ]
