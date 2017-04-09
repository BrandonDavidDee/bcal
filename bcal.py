import datetime
import itertools
from .models import Event


def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


def get_bcal(year, month):
    """ This function takes the requested year/month combo, gets a queryset for that month then
    iterates through the queryset, assigning objects with a datetime.day value to the date_range 
    dictionary. Then builds a simple HTML table-based month-view calendar """
    month_events = Event.objects.filter(date__year=year).filter(date__month=month)
    event_count = month_events.count()
    weekday_key = datetime.date(int(year), int(month), 1).weekday()
    is_leap = is_leap_year(int(year))
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
    """ I compared CPU time between dict.fromkeys and a traditional dictionary written out and 
    the time was identical so I chose the cleaner dict.fromkeys """
    date_range = dict.fromkeys(range(1, 32), '')

    """ Iterate through the Event month queryset and update dictionary with individual Event objects.
     day_link will be linked to a ListView that filters on the requested day. """
    for event in month_events:
        event_url = event.get_absolute_url()
        client = ' '.join([event.client.first_name, event.client.last_name])
        client = '<a href="%s">%s</a><br />' % (event_url, client)
        day = event.date.day

        for key, value in date_range.items():
            if key == day:
                date_range[day] += client

    """ Here we build the week based on the integer that represents the 1st day of the month.
     We build table rows 2-5 by iterating through slices of the date_range dictionary 
     with itertools.islice found beneath this if/else statement. Table row 1 (td1) gets special
     treatment because we are manually adding <td>&nbps;</td> to push the 1st of the month
     into it's correct day of week column. Finally Table row 6 (td6) gets an empty string
     when a sixth row isn't needed. Finally, the nested if/else statement that handles tr5 
     (and sometimes tr6) checks the requested month and if it's a leap year to determine the 
     final day of the month.
      """
    if weekday_key is 0:  # 1st falls on Monday -> example August 2016
        td1 = ""
        for key, value in itertools.islice(date_range.items(), 0, 6):
            x = ''.join(['<td>', str(key), '<br />', str(value), '</td>'])
            td1 += x

        td1 = '<td>&nbsp;</td>' + td1
        td2var1, td2var2 = 6, 13
        td3var1, td3var2 = 13, 20
        td4var1, td4var2 = 20, 27

        if month is '2' and is_leap is False:  # 28 days
            td5var1, td5var2 = 27, 28

        elif month is '2' and is_leap is True:  # 29 days
            td5var1, td5var2 = 27, 29

        elif month in thirties:  # 30 days
            td5var1, td5var2 = 27, 30

        else:  # 31 days
            td5var1, td5var2 = 27, 31

        td6 = ""

    elif weekday_key is 1:  # 1st falls on Tuesday -> example November 2016
        td1 = ""
        for key, value in itertools.islice(date_range.items(), 0, 5):
            x = ''.join(['<td>', str(key), '<br />', str(value), '</td>'])
            td1 += x
        td1 = '<td>&nbsp;</td><td>&nbsp;</td>' + td1
        td2var1, td2var2 = 5, 12
        td3var1, td3var2 = 12, 19
        td4var1, td4var2 = 19, 26

        if month is '2' and is_leap is False:  # 28 days
            td5var1, td5var2 = 26, 28

        elif month is '2' and is_leap is True:  # 29 days
            td5var1, td5var2 = 26, 29

        elif month in thirties:  # 30 days
            td5var1, td5var2 = 26, 30

        else:  # 31 days
            td5var1, td5var2 = 26, 31

        td6 = ""

    elif weekday_key is 2:  # 1st falls on Wednesday -> example February 2017
        td1 = ""
        for key, value in itertools.islice(date_range.items(), 0, 4):
            x = ''.join(['<td>', str(key), '<br />', str(value), '</td>'])
            td1 += x

        td1 = '<td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td>' + td1
        td2var1, td2var2 = 4, 11
        td3var1, td3var2 = 11, 18
        td4var1, td4var2 = 18, 25

        if month is '2' and is_leap is False:  # 28 days
            td5var1, td5var2 = 25, 28

        elif month is '2' and is_leap is True:  # 29 days
            td5var1, td5var2 = 25, 29

        elif month in thirties:  # 30 days
            td5var1, td5var2 = 25, 30

        else:  # 31 days
            td5var1, td5var2 = 25, 31

        td6 = ""

    elif weekday_key is 3:  # 1st falls on Thursday -> example Dec 2016
        td1 = ""
        for key, value in itertools.islice(date_range.items(), 0, 3):
            x = ''.join(['<td>', str(key), '<br />', str(value), '</td>'])
            td1 += x

        td1 = '<td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td>' + td1
        td2var1, td2var2 = 3, 10
        td3var1, td3var2 = 10, 17
        td4var1, td4var2 = 17, 24

        if month is '2' and is_leap is False:  # 28 days
            td5var1, td5var2 = 24, 28

        elif month is '2' and is_leap is True:  # 29 days
            td5var1, td5var2 = 24, 29

        elif month in thirties:  # 30 days
            td5var1, td5var2 = 24, 30

        else:  # 31 days
            td5var1, td5var2 = 24, 31

        td6 = ""

    elif weekday_key is 4:  # 1st falls on Friday -> example July 2016
        td1 = ""
        for key, value in itertools.islice(date_range.items(), 0, 2):
            x = ''.join(['<td>', str(key), '<br />', str(value), '</td>'])
            td1 += x

        td1 = '<td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td>' + td1
        td2var1, td2var2 = 2, 9
        td3var1, td3var2 = 9, 16
        td4var1, td4var2 = 16, 23

        if month is '2' and is_leap is False:  # 28 days
            td5var1, td5var2 = 24, 28
            td6 = ""

        elif month is '2' and is_leap is True:  # 29 days
            td5var1, td5var2 = 24, 29
            td6 = ""

        elif month in thirties:  # 30 days
            td5var1, td5var2 = 23, 30
            td6 = ""

        else:  # 31 days
            td5var1, td5var2 = 23, 30
            td6 = ""
            for key, value in itertools.islice(date_range.items(), 30, 31):
                x = ''.join(['<td>', str(key), '<br />', str(value), '</td>'])
                td6 += x

    elif weekday_key is 5:  # 1st falls on Saturday -> e.g. April 2017
        td1 = ""
        for key, value in itertools.islice(date_range.items(), 0, 1):
            x = ''.join(['<td>', str(key), '<br />', str(value), '</td>'])
            td1 += x
        td1 = '<td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td>' + td1
        td2var1, td2var2 = 1, 8
        td3var1, td3var2 = 8, 15
        td4var1, td4var2 = 15, 22

        if month is '2' and is_leap is False:  # 28 days
            td5var1, td5var2 = 22, 28
            td6 = ""

        elif month is '2' and is_leap is True:  # 29 days
            td5var1, td5var2 = 22, 29
            td6 = ""

        elif month in thirties:  # 30 days
            td5var1, td5var2 = 22, 29
            td6 = ""
            for key, value in itertools.islice(date_range.items(), 29, 30):
                x = ''.join(['<td>', str(key), '<br />', str(value), '</td>'])
                td6 += x

        else:  # 31 days
            td5var1, td5var2 = 22, 29
            td6 = ""
            for key, value in itertools.islice(date_range.items(), 29, 31):
                x = ''.join(['<td>', str(key), '<br />', str(value), '</td>'])
                td6 += x

    elif weekday_key is 6:  # 1st Falls on Sunday
        td1 = ""
        for key, value in itertools.islice(date_range.items(), 0, 7):
            x = ''.join(['<td>', str(key), '<br />', str(value), '</td>'])
            td1 += x

        td2var1, td2var2 = 7, 14
        td3var1, td3var2 = 14, 21
        td4var1, td4var2 = 21, 28

        if month is '2' and is_leap is False:  # 28 days
            td5var1, td5var2 = 0, 0

        elif month is '2' and is_leap is True:  # 29 days
            td5var1, td5var2 = 28, 29

        elif month in thirties:  # 30 days
            td5var1, td5var2 = 28, 30

        else:  # 31 days
            td5var1, td5var2 = 28, 31

        td6 = ""

    """ the iterators who's values are determined in the above if/else statement """
    td2 = ""
    for key, value in itertools.islice(date_range.items(), td2var1, td2var2):
        x = ''.join(['<td>', str(key), '<br />', str(value), '</td>'])
        td2 += x

    td3 = ""
    for key, value in itertools.islice(date_range.items(), td3var1, td3var2):
        x = ''.join(['<td>', str(key), '<br />', str(value), '</td>'])
        td3 += x

    td4 = ""
    for key, value in itertools.islice(date_range.items(), td4var1, td4var2):
        x = ''.join(['<td>', str(key), '<br />', str(value), '</td>'])
        td4 += x

    td5 = ""
    for key, value in itertools.islice(date_range.items(), td5var1, td5var2):
        x = ''.join(['<td>', str(key), '<br />', str(value), '</td>'])
        td5 += x

    """ Create Next Month and Previous Month Links """
    if month == '12':
        next_year = int(year) + 1
        next_month = 1
        ch1 = '<i class="fa fa-chevron-right" aria-hidden="true"></i>'
        next_month_link = '<a class="btn btn-default" href="/events/bcal/%s/%s/">%s</a>' % (next_year, next_month, ch1)
    else:
        next_month = int(month) + 1
        ch1 = '<i class="fa fa-chevron-right" aria-hidden="true"></i>'
        next_month_link = '<a class="btn btn-default" href="/events/bcal/%s/%s/">%s</a>' % (year, next_month, ch1)

    if month == '1':
        prev_year = int(year) - 1
        prev_month = 12
        ch2 = '<i class="fa fa-chevron-left" aria-hidden="true"></i>'
        prev_month_link = '<a class="btn btn-default" href="/events/bcal/%s/%s/">%s</a>' % (prev_year, prev_month, ch2)
    else:
        prev_month = int(month) - 1
        ch2 = '<i class="fa fa-chevron-left" aria-hidden="true"></i>'
        prev_month_link = '<a class="btn btn-default" href="/events/bcal/%s/%s/">%s</a>' % (year, prev_month, ch2)

    """ Join strings to build the complete table """
    header = ' '.join(['<h3>', month_name, year, '</h3>\n'])
    links = ''.join([prev_month_link, next_month_link, '<br /><br />'])
    table_open = '<table class="table table-bordered table-calendar">\n'
    head = '<tr><th>Sun</th><th>Mon</th><th>Tue</th><th>Wed</th><th>Thur</th><th>Fri</th><th>Sat</th></tr>\n'
    tr1 = '<tr>%s</tr>\n' % td1
    tr2 = '<tr>%s</tr>\n' % td2
    tr3 = '<tr>%s</tr>\n' % td3
    tr4 = '<tr>%s</tr>\n' % td4
    tr5 = '<tr>%s</tr>\n' % td5
    tr6 = '<tr>%s</tr>\n' % td6
    all_days = '%s%s%s%s%s%s' % (tr1, tr2, tr3, tr4, tr5, tr6)
    count = '%i events' % event_count
    table_close = '</table>'

    table = '%s%s%s%s%s%s%s' % (header, links, table_open, head, all_days, table_close, count)

    return table


