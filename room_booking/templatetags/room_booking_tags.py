from django import template

from room_booking.models import *

register = template.Library()


@register.inclusion_tag('room_booking/tags/rooms.html', takes_context=True)
def rooms(context):
    return {
        'rooms': Room.objects.all(),
        'request': context['request'],
    }


@register.inclusion_tag('room_booking/tags/bookings.html', takes_context=True)
def bookings(context):
    return {
        'bookings': Booking.objects.all(),
        'request': context['request'],
    }
