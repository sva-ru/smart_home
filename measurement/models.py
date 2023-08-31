from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, related_name='measurements', on_delete=models.CASCADE)
    temperature = models.FloatField()
    date_time = models.DateTimeField(auto_now_add=True)

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
