from django.db import models

# Create your models here.


class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

class NumberInput(models.Model):
    number1 = models.FloatField()
    number2 = models.FloatField()
