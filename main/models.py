from django.db import models

# Create your models here.
class VisitorCounter(models.Model):
    count = models.IntegerField(default=0)

class CurrencyRate(models.Model):
    currency = models.CharField(max_length=10)
    rate = models.FloatField()

class WeatherInfo(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    description = models.CharField(max_length=100)
