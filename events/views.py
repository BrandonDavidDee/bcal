import datetime

from django.contrib import messages
from django.shortcuts import render
from django.views.generic import DetailView, RedirectView

from events.bcal import get_bcal
from events.models import Event


def calendar(request, year, month, day):
    today = datetime.datetime.now()
    today_events = Event.objects.filter(date__year=year).filter(date__month=month).filter(date__day=day)
    if int(month) > 12:
        y = str(today.year)
        m = str(today.month)
        messages.add_message(request, messages.WARNING, 'Month error')
    else:
        y = year
        m = month

    return render(
        request,
        'calendar.html',
        {
            'calendar': get_bcal(y, m, day),
            'today': today_events,
        },
        content_type='html')


class CalendarRedirect(RedirectView):
    permanent = False
    today = datetime.datetime.now()
    url = '/events/calendar/%i/%i/%i' % (today.year, today.month, today.day)


class EventList(DetailView):
    model = Event
    template_name = 'event_detail.html'
