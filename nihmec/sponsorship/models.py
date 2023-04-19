from django.db import models
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.models import ClusterableModel
from django.utils.functional import cached_property
from wagtail.contrib.forms.panels import FormSubmissionsPanel
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.admin.panels import FieldPanel, InlinePanel, FieldRowPanel, MultiFieldPanel

# Create your models here.
@register_snippet
class SponsorshipPackageFeatures(models.Model):
    feature = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.feature



@register_snippet   
class SponsorshipPackage(ClusterableModel):
    sponsorship_type = models.CharField(max_length=100, help_text="e.g. Premium")
    price = models.DecimalField(decimal_places=2, null=True, max_digits=100)
    features = ParentalManyToManyField(SponsorshipPackageFeatures, related_name="package_features")

    panels = [
        FieldPanel('sponsorship_type'),
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
    template = 'sponsorship/sponsor.html'
    
    sponsorship_package = ParentalManyToManyField(SponsorshipPackage, blank=True)

    content_panels = Page.content_panels + [
        
        FieldPanel('sponsorship_package'),
        
    ]

    @cached_property
    def home_page(self):
        return self.get_parent().specific

    def get_context(self, request, *args, **kwargs):
        context = super(SponsorshipPage, self).get_context(request, *args, **kwargs)
        package_features = SponsorshipPackageFeatures.objects.all()
        context["package_features"] = package_features
        context["home_page"] = self.home_page
        return context


class SponsorDetail(Page):
    template = 'sponsorship/sponsor_detail.html'
    package = ParentalKey('SponsorshipPackage', on_delete=models.SET_NULL, related_name='sponsor_form_package', null=True)
    sponsor_form_page  = ParentalKey('SponsorFormPage', on_delete=models.SET_NULL, related_name='sponsor_form_page', null=True)

    content_panels = AbstractEmailForm.content_panels + [
        
        FieldPanel('package'),
        FieldPanel('sponsor_form_page'),
       
    ]

    @cached_property
    def home_page(self):
        return self.get_parent().specific

    def get_context(self, request, *args, **kwargs):
        context = super(SponsorDetail, self).get_context(request, *args, **kwargs)
        context["home_page"] = self.home_page
        return context


class FormField(AbstractFormField):
    page = ParentalKey('SponsorFormPage', on_delete=models.CASCADE, related_name='form_fields')


class SponsorFormPage(AbstractEmailForm):
    template = 'sponsorship/sponsor_detail.html'
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel('intro'),
        # FieldPanel('registration_package'),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]

    @cached_property
    def home_page(self):
        return self.get_parent().specific

    def get_context(self, request, *args, **kwargs):
        context = super(SponsorFormPage, self).get_context(request, *args, **kwargs)
        context["home_page"] = self.home_page
        return context

    def get_form_fields(self):
        return self.form_fields.all()