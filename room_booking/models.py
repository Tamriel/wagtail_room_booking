from django.db import models
from taggit.models import TaggedItemBase
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, \
    InlinePanel, PageChooserPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail.wagtailsnippets.models import register_snippet


@register_snippet
class Room(models.Model):
    name = models.CharField(max_length=255)
    capacity = models.IntegerField()
    # color todo
    # image todo

    panels = [
        FieldPanel('name'),
        FieldPanel('capacity'),
    ]

    def __str__(self):
        return self.name


class Booking(models.Model):
    """
    access from Room with .booking_set
    create from Room with .booking_set.create(title='My meeting')
    """
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)

    # date_time_from = models.DateTimeField()
    # date_time_to = models.DateTimeField()

    # description todo
    # user todo

    def __str__(self):
        return 'name: ' + self.room.name + 'title: ' + self.title + str(self.created)


# A couple of abstract classes that contain commonly used fields

class LinkFields(models.Model):
    link_external = models.URLField("External link", blank=True)
    link_page = models.ForeignKey(
            'wagtailcore.Page',
            null=True,
            blank=True,
            related_name='+'
    )
    link_document = models.ForeignKey(
            'wagtaildocs.Document',
            null=True,
            blank=True,
            related_name='+'
    )

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_document:
            return self.link_document.url
        else:
            return self.link_external

    panels = [
        FieldPanel('link_external'),
        PageChooserPanel('link_page'),
        DocumentChooserPanel('link_document'),
    ]

    class Meta:
        abstract = True


# Standard index page

class StandardIndexPage(Page):
    intro = RichTextField(blank=True)
    feed_image = models.ForeignKey(
            'wagtailimages.Image',
            null=True,
            blank=True,
            on_delete=models.SET_NULL,
            related_name='+'
    )

    search_fields = Page.search_fields + (
        index.SearchField('intro'),
    )


StandardIndexPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('intro', classname="full"),
]

StandardIndexPage.promote_panels = Page.promote_panels + [
    ImageChooserPanel('feed_image'),
]


# Standard page

class StandardPage(Page):
    body = RichTextField(blank=True)
    feed_image = models.ForeignKey(
            'wagtailimages.Image',
            null=True,
            blank=True,
            on_delete=models.SET_NULL,
            related_name='+'
    )

    search_fields = Page.search_fields + (
        index.SearchField('intro'),
        index.SearchField('body'),
    )


StandardPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('body', classname="full"),
]

StandardPage.promote_panels = Page.promote_panels + [
    ImageChooserPanel('feed_image'),
]


class RoomsWeekly(StandardPage):
    pass


class Rooms(StandardPage):
    pass
