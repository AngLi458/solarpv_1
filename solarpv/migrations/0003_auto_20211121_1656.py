# Generated by Django 2.2.24 on 2021-11-21 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solarpv', '0002_auto_20211025_1548'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='client',
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]