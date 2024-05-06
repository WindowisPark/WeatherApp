import requests
from django.conf import settings
from django.shortcuts import render

def get_weather_data(city_name):
    api_key = settings.API_KEY
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&units=metric&appid={api_key}"  
    response = requests.get(complete_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def weather(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        weather_data = get_weather_data(city)
        if weather_data:
            return render(request, 'weather.html', {'weather_data': weather_data})
        else:
            error_message = "Failed to retrieve weather data. Please try again later."
            return render(request, 'weather.html', {'error_message': error_message})
    else:
        return render(request, 'weather.html')

from django.shortcuts import redirect

