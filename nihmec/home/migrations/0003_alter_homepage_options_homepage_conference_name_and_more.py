# Generated by Django 4.1.8 on 2023-04-15 09:37

from django.db import migrations, models
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': 'Conference Page', 'verbose_name_plural': 'Conference Pages'},
        ),
        migrations.AddField(
            model_name='homepage',
            name='conference_name',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='contact_email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='contact_phone_number',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='feature_conference_on_site',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='short_description',
            field=wagtail.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='short_name',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='start_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='theme',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='venue',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='year',
            field=models.IntegerField(null=True, unique_for_year=True),
        ),
    ]