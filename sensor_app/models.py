from django.db import models
from django.utils import timezone


class SensorData(models.Model):
    datetime = models.DateTimeField(default=timezone.now)
    activity = models.CharField(max_length=100)
    status = models.IntegerField(default=0,editable=False)

    def __str__(self):
        return f"ID: {self.id}, Activity: {self.activity}"
