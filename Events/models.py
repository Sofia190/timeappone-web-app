from django.db import models

# Create your models here.

from Days.models import Day

from datetime import timedelta, datetime, date


class Event(models.Model):


	datetime_field = models.ManyToManyField(Day)
	event_name = models.CharField(max_length=500)
	event_description = models.TextField()






























