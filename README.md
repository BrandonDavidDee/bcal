# bcal
BCal is a Month-View calendar that displays Django objects with a datefield.

![alt tag](https://github.com/BrandonDavidDee/bcal/blob/master/bcal_screenshot.png)

### What's the purpose of this? Why not just use calendar.HTMLCalendar?

I needed a simple month-view calendar for a Django project. As a beginner I honestly felt a bit overwhelmed viewing the source for calendar.HTMLCalendar and trying to figure out how to work my model's objects into it. Also, I wanted the challenge of building something 100% python since at this point I've learned Django & Python simultaneously and feel I know more Django than I do Python (if that makes sense). So maybe this is redundant or unneccessary but since I wrote it I understand it and it's giving me opportunities to practice optimization as well.

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
