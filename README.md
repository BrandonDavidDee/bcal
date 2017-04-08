# bcal
BCal is a Month-View calendar that displays Django objects with a datefield.

![alt tag](https://github.com/BrandonDavidDee/bcal/blob/master/bcal_screenshot.png)

### What's the purpose of this? Why not just use calendar.HTMLCalendar?

I needed a simple month-view calendar for a Django project. As a beginner I honestly felt a bit overwhelmed viewing the source for calendar.HTMLCalendar and trying to figure out how to work my model's objects into it. Also, I wanted the challenge of building something 100% python since at this point I've learned Django & Python simultaneously and feel I know more Django than I do Python (if that makes sense). So maybe this is redundant or unneccessary but since I wrote it I understand it and it's giving me opportunities to practice optimization as well.

**Requirements:**
Python 3 (I haven't tested in Python 2)


#### Where it fits into my Django project:

**In models.py**

    class Event(models.Model):
        client = models.ForeignKey(settings.AUTH_USER_MODEL)
        date = models.DateField()
        

**In views.py**

    from django.shortcuts import render_to_response
    from .bcal import get_bcal
    ...
    def bcal(request, year, month):
    return render_to_response(
        'events/calendar.html',
        {'user': request.user, 'calendar': get_bcal(year, month)}
    )


**In urls.py**
    
    from .views import bcal
    ...
    url(r'^bcal/(?P<year>\d{4})/(?P<month>\d{1,2})/$', bcal, name='bcal'),
    ...
    
**In calendar.html**

    ...
    {{ calendar|safe }}
    ...


**In stylesheet**
The above screenshot is from a project with a Bootstrap3 base. Add the following styles if you want to keep the weekday columns from resizing around the objects:

    .table-calendar td:first-child {
      width: 14%;
    }

    .table-calendar td:nth-child(2) {
      width: 14%;
    }

    .table-calendar td:nth-child(3) {
      width: 14%;
    }

    .table-calendar td:nth-child(4) {
      width: 14%;
    }

    .table-calendar td:nth-child(5) {
      width: 14%;
    }

    .table-calendar td:nth-child(6) {
      width: 14%;
    }

    .table-calendar td:last-child {
      width: 14%;
    }
