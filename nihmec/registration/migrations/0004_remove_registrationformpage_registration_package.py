# Generated by Django 4.1.8 on 2023-04-17 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_rename_formpage_registrationformpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrationformpage',
            name='registration_package',
        ),
    ]
