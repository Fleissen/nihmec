from django.db import models

# Create your models here.
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.models import ClusterableModel
from django.utils.functional import cached_property

class AboutPage(Page):
    template = 'website/about.html'
    max_count = 1
    body = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]


    @cached_property
    def home_page(self):
        return self.get_parent().specific

    def get_context(self, request, *args, **kwargs):
        context = super(AboutPage, self).get_context(request, *args, **kwargs)
        context["home_page"] = self.home_page
        return context
    
    class Meta:
        verbose_name = 'About Page'
        verbose_name_plural = 'About Page'
    
class CallForAbstractPage(Page):
    template = 'website/call_for_abstract.html'
    max_count = 1
    body = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

    @cached_property
    def home_page(self):
        return self.get_parent().specific

    def get_context(self, request, *args, **kwargs):
        context = super(CallForAbstractPage, self).get_context(request, *args, **kwargs)
        context["home_page"] = self.home_page
        return context
    
    class Meta:
        verbose_name = 'Call for Abstract'
        verbose_name_plural = 'Call for Abstracts'

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

    class Meta:
        verbose_name = 'Speaker'
        verbose_name_plural = 'Speakers'

class SpeakersPage(Page):
    template = 'website/speakers.html'

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

    class Meta:
        verbose_name = 'Tecnical Advisory Committee'
        verbose_name_plural = 'Tecnical Advisory Committees'