from django.db import models

# Create your models here.
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey, ParentalManyToManyField



class Conference(Page):
    conference_name = models.CharField(max_length=500, null=True)
    short_name = models.CharField(max_length=500, null=True)
    year = models.IntegerField(unique_for_year=True, null=True)
    theme = models.CharField(max_length=1000, null=True)
    venue = models.CharField(max_length=1000, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    short_description = RichTextField(blank = True)
    contact_email = models.EmailField(null=True)
    contact_phone_number = models.CharField(max_length=20, null=True)
    feature_conference_on_site = models.BooleanField(default=True)

    content_panels = Page.content_panels + [
        FieldPanel('conference_name'),
        FieldPanel('year'),
        FieldPanel('theme'),
        FieldPanel('venue'),
        FieldPanel('start_date'),
        FieldPanel('end_date'),
        FieldPanel('short_description'),
    ]

    def __str__(self):
        return self.short_name

    class Meta:
        verbose_name_plural = 'Conference'

class AboutPage(Page):
    body = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

class CallForAbstractPage(Page):
    body = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]


@register_snippet
class SponsorshipPackageFeatures(models.Model):
    feature = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.feature
    
class SponsorshipPackage(Page):
    type = models.CharField(max_length=100, help_text="e.g. Premium")
    price = models.DecimalField(decimal_places=2, null=True, max_digits=7)
    features = ParentalManyToManyField(SponsorshipPackageFeatures, related_name="package_features")

    content_panels = Page.content_panels + [
        FieldPanel('type'),
        FieldPanel('price'),
        FieldPanel('features'),
    ]

class Sponsors(Page):
    package = ParentalKey(SponsorshipPackage, on_delete=models.SET_NULL, related_name='sponsor_package', null=True)
    company_name = models.CharField(max_length=500, null=True)
    first_name = models.CharField(max_length = 500, null=True, blank=True)
    surname = models.CharField(max_length=500, null=True, blank=True)
    position = models.CharField(max_length=500, null=True, blank=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=500, null=True, blank=True)
    state = models.CharField(max_length=500, null=True)
    country = models.CharField(max_length=500, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('package'),
        FieldPanel('company_name'),
        FieldPanel('first_name'),
        FieldPanel('surname'),
        FieldPanel('position'),
        FieldPanel('email'),
        FieldPanel('phone'),
        FieldPanel('city'),
        FieldPanel('state'),
        FieldPanel('country'),
        InlinePanel('companies_logos', label="Company Logos"),
    ]

class SponsorGalleryImage(Orderable):
    page = ParentalKey(Sponsors, on_delete=models.CASCADE, related_name='companies_logos')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]

@register_snippet
class RegistrationPackage(models.Model):
    option = models.CharField(max_length=200, help_text="e.g. Conference only", null=True)
    number_of_registrants = models.IntegerField(null=True)
    price = models.DecimalField(decimal_places=2, null=True, max_digits=6)
    panels = [
        FieldPanel('option'),
        FieldPanel('number_of_registrants'),
        FieldPanel('price'),
    ]
    def __str__(self):
        return self.option

class Registration(Page):
    registration_package = models.ForeignKey(RegistrationPackage, on_delete=models.SET_NULL, related_name='registration_package', null=True)
    first_name = models.CharField(max_length = 500, null=True, blank=True)
    surname = models.CharField(max_length=500, null=True, blank=True)
    SEX_CHOICES =( 
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    sex = models.CharField(max_length=20, null=True, choices=SEX_CHOICES)
    company = models.CharField(max_length=500, null=True)
    position = models.CharField(max_length=500, null=True, blank=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=500, null=True, blank=True)
    state = models.CharField(max_length=500, null=True)
    country = models.CharField(max_length=500, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('registration_package'),
        FieldPanel('first_name'),
        FieldPanel('surname'),
        FieldPanel('sex'),
        FieldPanel('company'),
        FieldPanel('position'),
        FieldPanel('email'),
        FieldPanel('phone'),
        FieldPanel('city'),
        FieldPanel('state'),
        FieldPanel('country'),
    ]


class Speakers(Page):
    first_name = models.CharField(max_length = 500, null=True, blank=True)
    surname = models.CharField(max_length=500, null=True, blank=True)
    company = models.CharField(max_length=500, null=True)
    position = models.CharField(max_length=500, null=True, blank=True)
    short_introduction = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('first_name'),
        FieldPanel('surname'),
        FieldPanel('company'),
        FieldPanel('position'),
        FieldPanel('short_introduction'),
        InlinePanel('speakers_photos', label="Speakers Photos"),
    ]

class SpeakerGalleryImage(Orderable):
    page = ParentalKey(Speakers, on_delete=models.CASCADE, related_name='speakers_photos')
    photo = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('photo'),
        FieldPanel('caption'),
    ]


class TechnicalAdvisoryCommittee(models.Model):
    first_name = models.CharField(max_length = 500, null=True, blank=True)
    surname = models.CharField(max_length=500, null=True, blank=True)
    company = models.CharField(max_length=500, null=True)
    position_in_company = models.CharField(max_length=500, null=True, blank=True)
    position_in_conference = models.CharField(max_length=500, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('first_name'),
        FieldPanel('surname'),
        FieldPanel('company'),
        FieldPanel('position_in_company'),
        FieldPanel('position_in_conference'),
        InlinePanel('committee_photos', label="Committee Photos"),
    ]

class CommitteeGalleryImage(Orderable):
    page = models.ForeignKey(TechnicalAdvisoryCommittee, on_delete=models.CASCADE, related_name='committee_photos')
    photo = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('photo'),
        FieldPanel('caption'),
    ]