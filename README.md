# bcal
BCal is a Month-View calendar that displays Django objects with a datefield.

Update: This repo has been updated to include bcal within the context of an entire Django project.

![alt tag](https://github.com/BrandonDavidDee/bcal/blob/master/bcal_screenshot3.png)

### What's the purpose of this? Why not just use calendar.HTMLCalendar?

Instead of trying to hack HTMLCalendar I wrote this calendar as a python exercise. It's builds itself by determining 3 things: What day of the week does the 1st fall on (datetime.weekday()), how many days are in that month and if it's a leap year (calendar.isleap()). This function iterates through a queryset of Event objects and based on their dates assigns them to a dictionary where the keys are days of the month and the values are the key as a string plus Event objects appended to it. Originally this was written to output an html table but it has been rewritten to output a Bootstrap4 grid. Also it now highlights the current day and allows individual days to be clicked on and highlighted as well. 

- see also: https://uggedal.com/journal/creating-a-flexible-monthly-calendar-in-django/

**Requirements:**
Python 3
Bootstrap4


#### Where it fits into my Django project:

**In models.py**

    class Client(models.Model):
        first_name = models.CharField(max_length=80)
        last_name = models.CharField(max_length=80)

        def __str__(self):
            return "%s %s" % (self.first_name, self.last_name)
        
    class Event(models.Model):
        client = models.ForeignKey(Client, on_delete=models.CASCADE)
        date = models.DateField()

        class Meta:
            verbose_name = 'event'
            ordering = ['date', 'client']
            get_latest_by = 'date'

        def __str__(self):
            return str(self.date)

        def get_absolute_url(self):
            return "/events/%i/" % self.id
        

**In views.py**

    from django.shortcuts import render
    from django.contrib import messages
    from .bcal import get_bcal
    ...

    def calendar(request, year, month, day):
        today = date.today()
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
            'events/calendar.html',
            {
                'calendar': get_bcal(y, m, day),
                'today': today_events,
            },
            content_type='html')


**In urls.py**
    
    from .views import bcal
    ...
    url(r'^calendar/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})$', calendar),
    or
    path('events/calendar/<year>/<month>/<day>/', calendar),
    ...
    
**In calendar.html**

    ...
    <div class="row">
        <div class="col-9">
            {{ calendar | safe }}
        </div>
        <div class="col-3">
            <h3>Events</h3>
            {% if today %}
                <ul>
                    {% for e in today %}
                        <li><a href="{{ e.get_absolute_url }}">{{ e.client }}</a></li>
                    {% endfor %}
                </ul>
            {% else %}
                No Events
            {% endif %}
        </div>
    </div>
    ...

**In your stylesheet**

The above screenshot is from a project with a Bootstrap4 base. Add the following styles to keep column heights at a minimum and to highlight current day and requested day:

    .cal-day {
        outline: .5px solid #cccccc;
        min-height: 100px;
        height: auto;
        margin: 1px;
    }

    #cal-req-day {
        background-color: #f5e1dd;
    }

    #cal-today {
        background-color: #e3e3e3;
    }
