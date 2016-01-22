from django.db import models
from taggit.models import TaggedItemBase
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField
from wagtail.wagtailsnippets.models import register_snippet
from cms.models import StandardPage


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


class RoomsWeekly(StandardPage):
    pass


class Rooms(StandardPage):
    pass
