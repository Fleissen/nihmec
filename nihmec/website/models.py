from django.db import models

# Create your models here.
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.models import ClusterableModel

class AboutPage(Page):
    template = 'about.html'
    max_count = 1
    body = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

class CallForAbstractPage(Page):
    template = 'call_for_abstract.html'
    max_count = 1
    body = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]


@register_snippet
class SponsorshipPackageFeatures(models.Model):
    feature = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.feature

@register_snippet   
class SponsorshipPackage(ClusterableModel):
    type = models.CharField(max_length=100, help_text="e.g. Premium")
    price = models.DecimalField(decimal_places=2, null=True, max_digits=100)
    features = ParentalManyToManyField(SponsorshipPackageFeatures, related_name="package_features")

    panels = [
        FieldPanel('type'),
        FieldPanel('price'),
        FieldPanel('features'),
    ]

@register_snippet
class Sponsors(models.Model):
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
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+', null=True
    )

    panels = [
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
        FieldPanel('image'),
    ]

class SponsorshipPage(Page):
    template = 'sponsor.html'

class SponsorDetail(Page):
    template = 'sponsor_detail.html'

@register_snippet
class RegistrationPackage(models.Model):
    option = models.CharField(max_length=200, help_text="e.g. Conference only", null=True)
    price = models.DecimalField(decimal_places=2, null=True, max_digits=100)
    panels = [
        FieldPanel('option'),
        FieldPanel('price'),
    ]
    def __str__(self):
        return self.option

@register_snippet
class Registration(models.Model):
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

    number_of_registrants = models.IntegerField(null=True, blank=True, default=1)

    panels = [
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
        FieldPanel('number_of_registrants'),
    ]

class RegistrationPage(Page):
    template = 'registration.html'
    

@register_snippet
class Speakers(models.Model):
    first_name = models.CharField(max_length = 500, null=True, blank=True)
    surname = models.CharField(max_length=500, null=True, blank=True)
    company = models.CharField(max_length=500, null=True)
    position = models.CharField(max_length=500, null=True, blank=True)
    short_introduction = RichTextField(blank=True)
    photo = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+', null=True
    )

    panels = [
        FieldPanel('first_name'),
        FieldPanel('surname'),
        FieldPanel('company'),
        FieldPanel('position'),
        FieldPanel('short_introduction'),
        FieldPanel('photo'),
    ]

class SpeakersPage(Page):
    template = 'speakers.html'

@register_snippet
class TechnicalAdvisoryCommittee(models.Model):
    first_name = models.CharField(max_length = 500, null=True, blank=True)
    surname = models.CharField(max_length=500, null=True, blank=True)
    company = models.CharField(max_length=500, null=True)
    position_in_company = models.CharField(max_length=500, null=True, blank=True)
    position_in_conference = models.CharField(max_length=500, null=True, blank=True)
    photo = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+', null=True
    )

    panels = [
        FieldPanel('first_name'),
        FieldPanel('surname'),
        FieldPanel('company'),
        FieldPanel('position_in_company'),
        FieldPanel('position_in_conference'),
        FieldPanel('photo'),
    ]