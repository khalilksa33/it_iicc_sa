from django.contrib import admin
from django.urls import path
from main.views import home, weather_info, currency_rates

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('weather/', weather_info, name='weather'),
    path('currency/', currency_rates, name='currency'),
]
