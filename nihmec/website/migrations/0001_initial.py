# Generated by Django 4.1.8 on 2023-04-14 16:30

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('wagtailcore', '0083_workflowcontenttype'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('body', wagtail.fields.RichTextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='CallForAbstractPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('body', wagtail.fields.RichTextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('conference_name', models.CharField(max_length=500, null=True)),
                ('short_name', models.CharField(max_length=500, null=True)),
                ('year', models.IntegerField(null=True, unique_for_year=True)),
                ('theme', models.CharField(max_length=1000, null=True)),
                ('venue', models.CharField(blank=True, max_length=1000, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('short_description', wagtail.fields.RichTextField(blank=True)),
                ('contact_email', models.EmailField(max_length=254, null=True)),
                ('contact_phone_number', models.CharField(max_length=20, null=True)),
                ('feature_conference_on_site', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Conference',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='RegistrationPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(help_text='e.g. Conference only', max_length=200, null=True)),
                ('number_of_registrants', models.IntegerField(null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Speakers',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('first_name', models.CharField(blank=True, max_length=500, null=True)),
                ('surname', models.CharField(blank=True, max_length=500, null=True)),
                ('company', models.CharField(max_length=500, null=True)),
                ('position', models.CharField(blank=True, max_length=500, null=True)),
                ('short_introduction', wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='SponsorshipPackageFeatures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TechnicalAdvisoryCommittee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=500, null=True)),
                ('surname', models.CharField(blank=True, max_length=500, null=True)),
                ('company', models.CharField(max_length=500, null=True)),
                ('position_in_company', models.CharField(blank=True, max_length=500, null=True)),
                ('position_in_conference', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SponsorshipPackage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('type', models.CharField(help_text='e.g. Premium', max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, null=True)),
                ('features', modelcluster.fields.ParentalManyToManyField(related_name='package_features', to='website.sponsorshippackagefeatures')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='Sponsors',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('company_name', models.CharField(max_length=500, null=True)),
                ('first_name', models.CharField(blank=True, max_length=500, null=True)),
                ('surname', models.CharField(blank=True, max_length=500, null=True)),
                ('position', models.CharField(blank=True, max_length=500, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone', models.CharField(max_length=20)),
                ('city', models.CharField(blank=True, max_length=500, null=True)),
                ('state', models.CharField(max_length=500, null=True)),
                ('country', models.CharField(blank=True, max_length=500, null=True)),
                ('package', modelcluster.fields.ParentalKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sponsor_package', to='website.sponsorshippackage')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='SponsorGalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('caption', models.CharField(blank=True, max_length=250)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.image')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='companies_logos', to='website.sponsors')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SpeakerGalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('caption', models.CharField(blank=True, max_length=250)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='speakers_photos', to='website.speakers')),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('first_name', models.CharField(blank=True, max_length=500, null=True)),
                ('surname', models.CharField(blank=True, max_length=500, null=True)),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20, null=True)),
                ('company', models.CharField(max_length=500, null=True)),
                ('position', models.CharField(blank=True, max_length=500, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone', models.CharField(max_length=20)),
                ('city', models.CharField(blank=True, max_length=500, null=True)),
                ('state', models.CharField(max_length=500, null=True)),
                ('country', models.CharField(blank=True, max_length=500, null=True)),
                ('registration_package', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='registration_package', to='website.registrationpackage')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='CommitteeGalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('caption', models.CharField(blank=True, max_length=250)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='committee_photos', to='website.technicaladvisorycommittee')),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
