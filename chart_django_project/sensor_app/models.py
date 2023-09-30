from django.db import models

class SensorData(models.Model):
    datetime = models.DateTimeField()
    activity = models.CharField(max_length=100)
