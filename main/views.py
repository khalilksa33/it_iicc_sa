from django.shortcuts import render
from django.http import JsonResponse
from .models import VisitorCounter, CurrencyRate, WeatherInfo
from django.utils import timezone
import requests

def home(request):
    visitor_counter, created = VisitorCounter.objects.get_or_create(id=1)
    visitor_counter.count += 1
    visitor_counter.save()

    context = {
        'current_date': timezone.now(),
        'visitor_count': visitor_counter.count,
    }
    return render(request, 'main/home.html', context)

def weather_info(request):
    response = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Medina=2648f48384fff719c6ae4789d789882f')
    data = response.json()
    weather_info = WeatherInfo.objects.create(
        city=data['name'],
        temperature=data['main']['temp'],
        description=data['weather'][0]['description']
    )
    context = {
        'weather': weather_info
    }
    return render(request, 'main/weather.html', context)

def currency_rates(request):
    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    data = response.json()
    for currency, rate in data['rates'].items():
        CurrencyRate.objects.create(currency=currency, rate=rate)
    return JsonResponse(data)
