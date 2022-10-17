from django.http import HttpResponse
from django.shortcuts import render
import requests
import datetime

# Create your views here.
def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Dhaka'
    
    appid = '0faa80c009344f0aa1cb84a97b8f3b3e'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q':city, 'appid':appid, 'units':'metric'}
    r = requests.get(url=URL, params=PARAMS)
    res = r.json()
    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']
    day = datetime.date.today()

    contex = {
        'description':description,
        'icon':icon,
        'temp':temp,
        'day':day,
        'city':city
    }


    return render(request, 'weather/index.html', contex)
