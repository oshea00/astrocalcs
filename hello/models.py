from django.db import models

# Create your models here.


class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

class EasterInput(models.Model):
    year = models.FloatField()

class JulianInput(models.Model):
    year = models.FloatField()
    month = models.FloatField()
    day = models.FloatField()
    hour = models.FloatField()
    minute = models.FloatField()
    seconds = models.FloatField()
