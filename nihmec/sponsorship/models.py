from django.db import models
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.models import ClusterableModel

# Create your models here.
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

    class Meta:
        verbose_name = 'Sponsor'
        verbose_name_plural = 'Sponsors'

class SponsorshipPage(Page):
    template = 'sponsor.html'

class SponsorDetail(Page):
    template = 'sponsor_detail.html'