# Generated by Django 2.2.24 on 2021-10-25 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solarpv', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='client_id',
            new_name='client',
        ),
    ]
