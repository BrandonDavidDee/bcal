from calendar import isleap
import datetime
import itertools
from .models import Event


def get_bcal(year, month, day):
    request_day = day
    today = datetime.datetime.today()
    current_month = str(today.month)
    current_year = str(today.year)
    month_events = Event.objects.filter(date__year=year).filter(date__month=month)
    weekday_key = datetime.date(int(year), int(month), 1).weekday()
    is_leap = isleap(int(year))
    month_list = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }
    month_name = month_list[int(month)]
    thirties = ('4', '6', '9', '11')
    date_range = dict.fromkeys(range(1, 32), '')
    """ Iterate through the Event month queryset and update dictionary with individual Event objects.
     day_link will be linked to a ListView that filters on the requested day. """
    for event in month_events:
        event_url = event.get_absolute_url()
        client = ' '.join([event.client.first_name, event.client.last_name])
        client = '<small><a href="%s">%s</a></small><br />' % (event_url, client)
        day = event.date.day
        for key, value in date_range.items():
            if key == day:
                date_range[day] += client
    row_today = "<div id=\"cal-today\" class=\"col cal-day\"><a href=\"/events/calendar/%s/%s/%s\">%s</a><br />%s</div>"
    row_request_day = "<div id=\"cal-req-day\" class=\"col cal-day\">%s<br />%s</div>"
    row_day = "<div class=\"col cal-day\"><a href=\"/events/calendar/%s/%s/%s\">%s</a><br />%s</div>"
    empty_day = "<div class =\"col cal-day\">&nbsp;</div>"
    sixth_row = False

    if weekday_key is 0:  # 1st falls on Monday -> example August 2016
        row1 = ""
        before = empty_day
        for key, value in itertools.islice(date_range.items(), 0, 6):
            if year == current_year and month == current_month and key == today.day:
                row1 += row_today % (year, month, key, key, str(value))
            elif str(key) == request_day:
                row1 += row_request_day % (str(key), str(value))
            else:
                row1 += row_day % (year, month, key, key, str(value))
        row1 = "%s%s" % (before, row1)
        row2 = ""
        for key, value in itertools.islice(date_range.items(), 6, 13):
            if year == current_year and month == current_month and key == today.day:
                row2 += row_today % (year, month, key, key, str(value))
            elif str(key) == request_day:
                row2 += row_request_day % (str(key), str(value))
            else:
                row2 += row_day % (year, month, key, key, str(value))
        row3 = ""
        for key, value in itertools.islice(date_range.items(), 13, 20):
            if year == current_year and month == current_month and key == today.day:
                row3 += row_today % (year, month, key, key, str(value))
            elif str(key) == request_day:
                row3 += row_request_day % (str(key), str(value))
            else:
                row3 += row_day % (year, month, key, key, str(value))
        row4 = ""
        for key, value in itertools.islice(date_range.items(), 20, 27):
            if year == current_year and month == current_month and key == today.day:
                row4 += row_today % (year, month, key, key, str(value))
            elif str(key) == request_day:
                row4 += row_request_day % (str(key), str(value))
            else:
                row4 += row_day % (year, month, key, key, str(value))
        row5 = ""
        if month is '2' and is_leap is False:  # 28 days
            start, end = 27, 28
            remainder = empty_day * 6
        elif month is '2' and is_leap is True:  # 29 days
            start, end = 27, 29
            remainder = empty_day * 5
        elif month in thirties:  # 30 days
            start, end = 27, 30
            remainder = empty_day * 4
        else:  # 31 days
            start, end = 27, 31
            remainder = empty_day * 3
        for key, value in itertools.islice(date_range.items(), start, end):
            if year == current_year and month == current_month and key == today.day:
                row5 += row_today % (year, month, key, key, str(value))
            elif str(key) == request_day:
                row5 += row_request_day % (str(key), str(value))
            else:
                row5 += row_day % (year, month, key, key, str(value))
        row5 = "%s%s" % (row5, remainder)

    elif weekday_key is 1:  # 1st falls on Tuesday -> example November 2016
        row1 = ""
        before = empty_day * 2
        for key, value in itertools.islice(date_range.items(), 0, 5):
            if year == current_year and month == current_month and key == today.day:
                row1 += row_today % (year, month, key, key, str(value))
            elif str(key) == request_day:
                row1 += row_request_day % (str(key), str(value))
            else:
                row1 += row_day % (year, month, key, key, str(value))
        row1 = "%s%s" % (before, row1)
        row2 = ""
        for key, value in itertools.islice(date_range.items(), 5, 12):
            if year == current_year and month == current_month and key == today.day:
                row2 += row_today % (year, month, key, key, str(value))
            elif str(key) == request_day:
                row2 += row_request_day % (str(key), str(value))
            else:
                row2 += row_day % (year, month, key, key, str(value))
        row3 = ""
        for key, value in itertools.islice(date_range.items(), 12, 19):
            if year == current_year and month == current_month and key == today.day:
                row3 += row_today % (year, month, key, key, str(value))
            elif str(key) == request_day:
                row3 += row_request_day % (str(key), str(value))
            else:
                row3 += row_day % (year, month, key, key, str(value))
        row4 = ""
        for key, value in itertools.islice(date_range.items(), 19, 26):
            if year == current_year and month == current_month and key == today.day:
                row4 += row_today % (year, month, key, key, str(value))
            elif str(key) == request_day:
                row4 += row_request_day % (str(key), str(value))
            else:
                row4 += row_day % (year, month, key, key, str(value))
        row5 = ""
        if month is '2' and is_leap is False:  # 28 days
            start, end = 26, 28
            remainder = empty_day * 5
        elif month is '2' and is_leap is True:  # 29 days
            start, end = 26, 29
            remainder = empty_day * 4
        elif month in thirties:  # 30 days
            start, end = 26, 30
            remainder = empty_day * 3
        else:  # 31 days
            start, end = 26, 31
            remainder = empty_day * 2
        for key, value in itertools.islice(date_range.items(), start, end):
            if year == current_year and month == current_month and key == today.day:
                row5 += row_today % (year, month, key, key, str(value))
            elif str(key) == request_day:
                row5 += row_request_day % (str(key), str(value))
            else:
                row5 += row_day % (year, month, key, key, str(value))
        row5 = "%s%s" % (row5, remainder)

    elif weekday_key is 2:  # 1st falls on Wednesday -> example February 2017

        row1 = ""
        before = empty_day * 3
        for key, value in itertools.islice(date_range.items(), 0, 4):
            if year == current_year and month == current_month and key == today.day:
                row1 += row_today % (year, month, key, key, str(value))
            elif str(key) == request_day:
                row1 += row_request_day % (str(key), str(value))
            else:
                row1 += row_day % (year, month, key, key, str(value))
        row1 = "%s%s" % (before, row1)
        row2 = ""
        for key, value in itertools.islice(date_range.items(), 4, 11):
            if year == current_year and month == current_month and key == today.day:
                row2 += row_today % (year, month, key, key, str(value))
            elif str(key) == request_day:
                row2 += row_request_day % (str(key), str(value))
            else:
                row2 += row_day % (year, month, key, key, str(value))
        row3 = ""
        for key, value in itertools.islice(date_range.items(), 11, 18):
            if year == current_year and month == current_month and key == today.day:
                row3 += row_today % (year, month, key, key, str(value))
            elif str(key) == request_day:
                row3 += row_request_day % (str(key), str(value))
            else:
                row3 += row_day % (year, month, key, key, str(value))
        row4 = ""
        for key, value in itertools.islice(date_range.items(), 18, 25):
            if year == current_year and month == current_month and key == today.day:
                row4 += row_today % (year, month, key, key, str(value))
            elif str(key) == request_day:
                row4 += row_request_day % (str(key), str(value))
            else:
                row4 += row_day % (year, month, key, key, str(value))
        row5 = ""
        if month is '2' and is_leap is False:  # 28 days
            start, end = 25, 28
            remainder = empty_day * 4
        elif month is '2' and is_leap is True:  # 29 days
            start, end = 25, 29
            remainder = empty_day * 3
        elif month in thirties:  # 30 days
            start, end = 25, 30
            remainder = empty_day * 2
        else:  # 31 days
            start, end = 25, 31
            remainder = empty_day * 1
        for key, value in itertools.islice(date_range.items(), start, end):
            if year == current_year and month == current_month and key == today.day:
                row5 += row_today % (year, month, key, key, str(value))
            elif str(key) == request_day:
                row5 += row_request_day % (str(key), str(value))
            else:
                row5 += row_day % (year, month, key, key, str(value))
        row5 = "%s%s" % (row5, remainder)

    elif weekday_key is 3:  # 1st falls on Thursday -> example Dec 2016
        row1 = ""
        before = empty_day * 4
        for key, value in itertools.islice(date_range.items(), 0, 3):
            if year == current_year and month == current_month and key == today.day:
                row1 += row_today % (year, month, key, key, str(value))
            elif str(key) == request_day:
                row1 += row_request_day % (str(key), str(value))
            else:
                row1 += row_day % (year, month, key, key, str(value))
        row1 = "%s%s" % (before, row1)
        row2 = ""
        for key, value in itertools.islice(date_range.items(), 3, 10):
            if year == current_year and month == current_month and key == today.day:
                row2 += row_today % (year, month, key, key, str(value))
            elif str(key) == request_day:
                row2 += row_request_day % (str(key), str(value))
            else:
                row2 += row_day % (year, month, key, key, str(value))
        row3 = ""
        for key, value in itertools.islice(date_range.items(), 10, 17):
            if year == current_year and month == current_month and key == today.day:
                row3 += row_today % (year, month, key, key, str(value))
            elif str(key) == request_day:
                row3 += row_request_day % (str(key), str(value))
            else:
                row3 += row_day % (year, month, key, key, str(value))
        row4 = ""
        for key, value in itertools.islice(date_range.items(), 17, 24):
            if year == current_year and month == current_month and key == today.day:
                row4 += row_today % (year, month, key, key, str(value))
            elif str(key) == request_day:
                row4 += row_request_day % (str(key), str(value))
            else:
                row4 += row_day % (year, month, key, key, str(value))
        row5 = ""
        if month is '2' and is_leap is False:  # 28 days
            start, end = 24, 28
            remainder = empty_day * 3
        elif month is '2' and is_leap is True:  # 29 days
            start, end = 24, 29
            remainder = empty_day * 2
        elif month in thirties:  # 30 days
            start, end = 24, 30
            remainder = empty_day * 1
        else:  # 31 days
            start, end = 24, 31
            remainder = ""
        for key, value in itertools.islice(date_range.items(), start, end):
            if year == current_year and month == current_month and key == today.day:
                row5 += row_today % (year, month, key, key, str(value))
            elif str(key) == request_day:
                row5 += row_request_day % (str(key), str(value))
            else:
                row5 += row_day % (year, month, key, key, str(value))
        row5 = "%s%s" % (row5, remainder)

    elif weekday_key is 4:  # 1st falls on Friday -> example July 2016
        row1 = ""
        before = empty_day * 5
        for key, value in itertools.islice(date_range.items(), 0, 2):
            if year == current_year and month == current_month and key == today.day:
                row1 += row_today % (year, month, key, key, str(value))
            elif str(key) == request_day:
                row1 += row_request_day % (str(key), str(value))
            else:
                row1 += row_day % (year, month, key, key, str(value))
        row1 = "%s%s" % (before, row1)
        row2 = ""
        for key, value in itertools.islice(date_range.items(), 2, 9):
            if year == current_year and month == current_month and key == today.day:
                row2 += row_today % (year, month, key, key, str(value))
            elif str(key) == request_day:
                row2 += row_request_day % (str(key), str(value))
            else:
                row2 += row_day % (year, month, key, key, str(value))
        row3 = ""
        for key, value in itertools.islice(date_range.items(), 9, 16):
            if year == current_year and month == current_month and key == today.day:
                row3 += row_today % (year, month, key, key, str(value))
            elif str(key) == request_day:
                row3 += row_request_day % (str(key), str(value))
            else:
                row3 += row_day % (year, month, key, key, str(value))
        row4 = ""
        for key, value in itertools.islice(date_range.items(), 16, 23):
            if year == current_year and month == current_month and key == today.day:
                row4 += row_today % (year, month, key, key, str(value))
            elif str(key) == request_day:
                row4 += row_request_day % (str(key), str(value))
            else:
                row4 += row_day % (year, month, key, key, str(value))
        row5 = ""
        if month is '2' and is_leap is False:  # 28 days
            start, end = 23, 28
            remainder = empty_day * 2
        elif month is '2' and is_leap is True:  # 29 days
            start, end = 23, 29
            remainder = empty_day * 1
        elif month in thirties:  # 30 days
            start, end = 23, 30
            remainder = ""
        else:  # 31 days
            start, end = 23, 30
            remainder = ""
            sixth_row = True
        for key, value in itertools.islice(date_range.items(), start, end):
            if year == current_year and month == current_month and key == today.day:
                row5 += row_today % (year, month, key, key, str(value))
            elif str(key) == request_day:
                row5 += row_request_day % (str(key), str(value))
            else:
                row5 += row_day % (year, month, key, key, str(value))
        row5 = "%s%s" % (row5, remainder)
        if sixth_row:
            row6 = ""
            remainder = empty_day * 6
            for key, value in itertools.islice(date_range.items(), 30, 31):
                if year == current_year and month == current_month and key == today.day:
                    row6 += row_today % (year, month, key, key, str(value))
                elif str(key) == request_day:
                    row6 += row_request_day % (
                        str(key), str(value))
                else:
                    row6 += row_day % (year, month, key, key, str(value))
            row6 = "%s%s" % (row6, remainder)

    elif weekday_key is 5:  # 1st falls on Saturday -> e.g. April 2017
        row1 = ""
        before = empty_day * 6
        for key, value in itertools.islice(date_range.items(), 0, 1):
            if year == current_year and month == current_month and key == today.day:
                row1 += row_today % (year, month, key, key, str(value))
            elif str(key) == request_day:
                row1 += row_request_day % (str(key), str(value))
            else:
                row1 += row_day % (year, month, key, key, str(value))
        row1 = "%s%s" % (before, row1)
        row2 = ""
        for key, value in itertools.islice(date_range.items(), 1, 8):
            if year == current_year and month == current_month and key == today.day:
                row2 += row_today % (year, month, key, key, str(value))
            elif str(key) == request_day:
                row2 += row_request_day % (str(key), str(value))
            else:
                row2 += row_day % (year, month, key, key, str(value))
        row3 = ""
        for key, value in itertools.islice(date_range.items(), 8, 15):
            if year == current_year and month == current_month and key == today.day:
                row3 += row_today % (year, month, key, key, str(value))
            elif str(key) == request_day:
                row3 += row_request_day % (str(key), str(value))
            else:
                row3 += row_day % (year, month, key, key, str(value))
        row4 = ""
        for key, value in itertools.islice(date_range.items(), 15, 22):
            if year == current_year and month == current_month and key == today.day:
                row4 += row_today % (year, month, key, key, str(value))
            elif str(key) == request_day:
                row4 += row_request_day % (str(key), str(value))
            else:
                row4 += row_day % (year, month, key, key, str(value))
        row5 = ""
        if month is '2' and is_leap is False:  # 28 days
            start, end = 22, 28
            remainder = empty_day * 1
        elif month is '2' and is_leap is True:  # 29 days
            start, end = 22, 29
            remainder = ""
        elif month in thirties:  # 30 days
            start, end = 22, 29
            remainder = ""
            sixth_row = True
            row6start, row6end = 29, 30
            row6remainder = empty_day * 6
        else:  # 31 days
            start, end = 22, 29
            remainder = ""
            sixth_row = True
            row6start, row6end = 29, 31
            row6remainder = empty_day * 5
        for key, value in itertools.islice(date_range.items(), start, end):
            if year == current_year and month == current_month and key == today.day:
                row5 += row_today % (year, month, key, key, str(value))
            elif str(key) == request_day:
                row5 += row_request_day % (str(key), str(value))
            else:
                row5 += row_day % (year, month, key, key, str(value))
        row5 = "%s%s" % (row5, remainder)
        if sixth_row:
            row6 = ""
            for key, value in itertools.islice(date_range.items(), row6start,
                                               row6end):
                if year == current_year and month == current_month and key == today.day:
                    row6 += row_today % (year, month, key, key, str(value))
                elif str(key) == request_day:
                    row6 += row_request_day % (
                        str(key), str(value))
                else:
                    row6 += row_day % (year, month, key, key, str(value))
            row6 = "%s%s" % (row6, row6remainder)

    elif weekday_key is 6:  # 1st Falls on Sunday --> October 2017
        row1 = ""
        for key, value in itertools.islice(date_range.items(), 0, 7):
            if year == current_year and month == current_month and key == today.day:
                row1 += row_today % (year, month, key, key, str(value))
            elif str(key) == request_day:
                row1 += row_request_day % (str(key), str(value))
            else:
                row1 += row_day % (year, month, key, key, str(value))
        row2 = ""
        for key, value in itertools.islice(date_range.items(), 7, 14):
            if year == current_year and month == current_month and key == today.day:
                row2 += row_today % (year, month, key, key, str(value))
            elif str(key) == request_day:
                row2 += row_request_day % (str(key), str(value))
            else:
                row2 += row_day % (year, month, key, key, str(value))
        row3 = ""
        for key, value in itertools.islice(date_range.items(), 14, 21):
            if year == current_year and month == current_month and key == today.day:
                row3 += row_today % (year, month, key, key, str(value))
            elif str(key) == request_day:
                row3 += row_request_day % (str(key), str(value))
            else:
                row3 += row_day % (year, month, key, key, str(value))
        row4 = ""
        for key, value in itertools.islice(date_range.items(), 21, 28):
            if year == current_year and month == current_month and key == today.day:
                row4 += row_today % (year, month, key, key, str(value))
            elif str(key) == request_day:
                row4 += row_request_day % (str(key), str(value))
            else:
                row4 += row_day % (year, month, key, key, str(value))
        row5 = ""
        if month is '2' and is_leap is False:  # 28 days
            start, end = 28, 28
            remainder = ""
        elif month is '2' and is_leap is True:  # 29 days
            start, end = 28, 29
            remainder = empty_day * 6
        elif month in thirties:  # 30 days
            start, end = 28, 30
            remainder = empty_day * 5
        else:  # 31 days
            start, end = 28, 31
            remainder = empty_day * 4
        for key, value in itertools.islice(date_range.items(), start, end):
            if year == current_year and month == current_month and key == today.day:
                row5 += row_today % (year, month, key, key, str(value))
            elif str(key) == request_day:
                row5 += row_request_day % (str(key), str(value))
            else:
                row5 += row_day % (year, month, key, key, str(value))
        row5 = "%s%s" % (row5, remainder)
    # Create Next Month and Previous Month Links
    nav = '<a class="btn btn-default" href="/events/calendar/%s/%s/1">%s</a>'
    right_chevron = '<i class="fa fa-chevron-right" aria-hidden="true"></i>'
    left_chevron = '<i class="fa fa-chevron-left" aria-hidden="true"></i>'
    if month == '12':
        next_year = int(year) + 1
        next_month = 1
        ch1 = right_chevron
        next_month_link = nav % (next_year, next_month, ch1)
    else:
        next_month = int(month) + 1
        ch1 = right_chevron
        next_month_link = nav % (year, next_month, ch1)

    if month == '1':
        prev_year = int(year) - 1
        prev_month = 12
        ch2 = left_chevron
        prev_month_link = nav % (prev_year, prev_month, ch2)
    else:
        prev_month = int(month) - 1
        ch2 = left_chevron
        prev_month_link = nav % (year, prev_month, ch2)

    links = "<h3>%s %s %s %s%s</h3>" % (
        month_name, request_day, year, prev_month_link, next_month_link
    )
    sun = "<div class=\"col cal-header\">Sunday</div>\n"
    mon = "<div class=\"col cal-header\">Monday</div>\n"
    tue = "<div class=\"col cal-header\">Tuesday</div>\n"
    wed = "<div class=\"col cal-header\">Wednesday</div>\n"
    thu = "<div class=\"col cal-header\">Thursday</div>\n"
    fri = "<div class=\"col cal-header\">Friday</div>\n"
    sat = "<div class=\"col cal-header\">Saturday</div>\n"
    header = "<div class=\"row\">%s%s%s%s%s%s%s</div>\n" % (
        sun, mon, tue, wed, thu, fri, sat
    )
    one = "<div class=\"row\">%s</div>\n" % row1
    two = "<div class=\"row\">%s</div>\n" % row2
    three = "<div class=\"row\">%s</div>\n" % row3
    four = "<div class=\"row\">%s</div>\n" % row4
    five = "<div class=\"row\">%s</div>\n" % row5
    if sixth_row:
        six = "<div class=\"row\">%s</div>\n" % row6
        return "%s%s%s%s%s%s%s%s" % (
        links, header, one, two, three, four, five, six
        )
    else:
        return "%s%s%s%s%s%s%s" % (links, header, one, two, three, four, five)
