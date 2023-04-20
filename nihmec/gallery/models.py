from django.db import models
from modelcluster.fields import ParentalKey

from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel, InlinePanel

# Create your models here.

class ConferenceYearPage(Page):
    year = models.CharField(max_length=4)

    content_panels = Page.content_panels + [
        FieldPanel('year'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]

class ConferenceGalleryImage(Orderable):
    page = ParentalKey(ConferenceYearPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]