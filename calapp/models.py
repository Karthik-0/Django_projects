from django.db import models
from model_utils.models import TimeStampedModel
from taggit.managers import TaggableManager
# from django.conf import settings
import datetime


class EventTime(models.Model):
    start_time = models.TimeField(
        auto_now=False,
        auto_now_add=False,
        blank=True,
        null=True
        )
    end_time = models.TimeField(
        auto_now=False,
        auto_now_add=False,
        blank=True,
        null=True
        )
    duration = models.DurationField(blank=True, default=0)
    all_day = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if (self.start_time and self.end_time) is not None:
            start = self.start_time
            end = self.end_time
            start_delta = datetime.timedelta(
                hours=start.hour,
                minutes=start.minute,
                seconds=start.second)
            end_delta = datetime.timedelta(
                hours=end.hour,
                minutes=end.minute,
                seconds=end.second)
            self.duration = end_delta - start_delta
        # print(difference_delta)
        super(EventTime, self).save(*args, **kwargs)

    def __str__(self):
        return '{} {} {} {}'.format(
            self.start_time,
            self.end_time,
            self.duration,
            self.all_day)


class Entry(TimeStampedModel):
    name = models.CharField(max_length=100)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL,
    #                          on_delete=models.CASCADE)
    date = models.DateField()
    time = models.ManyToManyField("calapp.EventTime")
    description = models.TextField()
    place = models.ForeignKey("placesapp.Place", on_delete=models.CASCADE)
    tags = TaggableManager()

    def __str__(self):
        return '{} {}'.format(self.name, self.date)
