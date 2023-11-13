from django.db import models

class WeatherData(models.Model):
    timestamp = models.DateTimeField()
    temperature = models.FloatField(null=True)
    humidity = models.FloatField(null=True)
    rain = models.FloatField(null=True)
    ldr = models.FloatField(null=True)
    moisture = models.FloatField(null=True)

    def __str__(self):
        return f"{self.timestamp} - {self.temperature} - {self.humidity} - {self.rain} - {self.ldr} - {self.moisture}"
