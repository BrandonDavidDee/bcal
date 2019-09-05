from django.db import models


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
