# Generated by Django 4.1.8 on 2023-04-21 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0083_workflowcontenttype'),
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ConferenceYearPage',
            new_name='GalleryYearPage',
        ),
    ]