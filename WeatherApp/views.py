# views.py
from django.shortcuts import render
from django.http import HttpResponse
import requests

def home(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        api_key =os.environ.get ('507dcae6d33751f955b6126301546a65')
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=507dcae6d33751f955b6126301546a65'
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            weather_data = {
                'city': data['name'],
                'state': data['sys']['country'],  # Assuming the state information is in the 'country' field
                'main': data['weather'][0]['main'],
                'temp_celsius': round(data['main']['temp'] - 273.15, 2),
                'temp_fahrenheit': round((data['main']['temp'] - 273.15) * 9 / 5 + 32, 2),
            }
            return render(request, 'weather/weather.html', weather_data)
        else:
            return render(request, 'weather/error.html', {'error_message': 'City not found'})
    
    return render(request, 'weather/index.html', {})


# Create your views here.

