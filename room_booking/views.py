from django.core.urlresolvers import resolve
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.conf import settings

from .models import Room


def book(request, room_id):
    if request.user.is_authenticated():
        room = get_object_or_404(Room, pk=room_id)
        # todo check if time is not used
        room.booking_set.create(title=request.POST['title'])
        return HttpResponseRedirect(settings.WEEKLY_VIEW_URL)
    else:
        return HttpResponse('Du bist nicht angemeldet.', status=403)


def booking_page(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    return render(request, 'room_booking/booking_page.html', {'room': room})