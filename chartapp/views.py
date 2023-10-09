from django.http import JsonResponse
from django.shortcuts import render
from .models import WeatherData
from django.utils import timezone

# https://sensor-and-chart.onrender.com/chart_data/?temperature=value&humidity=value&rain=value&ldr=value
def chart_data_view(request):
    temperature = request.GET.get('temperature', None)
    humidity = request.GET.get('humidity', None)
    rain = request.GET.get('rain', None)
    ldr = request.GET.get('ldr', None)

    # Create a dictionary to store the data you want to save
    data_to_save = {
        'timestamp': timezone.now(),
        'temperature': temperature,
        'humidity': humidity,
        'rain': rain,
        'ldr': ldr,
    }

    # Remove None values from the dictionary
    data_to_save = {k: v for k, v in data_to_save.items() if v is not None}

    # Create a new entry in the database using the data
    WeatherData.objects.create(**data_to_save)

    return JsonResponse({"message": "Data saved successfully"})



def weather_data_view(request):
    # Get the data for each field
    temperature_data = WeatherData.objects.values_list('timestamp', 'temperature')
    humidity_data = WeatherData.objects.values_list('timestamp', 'humidity')
    rain_data = WeatherData.objects.values_list('timestamp', 'rain')
    ldr_data = WeatherData.objects.values_list('timestamp', 'ldr')

    # Prepare the data in a format suitable for Chart.js
    temperature_labels = [entry[0].strftime('%H:%M:%S') for entry in temperature_data]
    temperature_values = [entry[1] for entry in temperature_data]

    humidity_labels = [entry[0].strftime('%H:%M:%S') for entry in humidity_data]
    humidity_values = [entry[1] for entry in humidity_data]

    rain_labels = [entry[0].strftime('%H:%M:%S') for entry in rain_data]
    rain_values = [entry[1] for entry in rain_data]

    ldr_labels = [entry[0].strftime('%H:%M:%S') for entry in ldr_data]
    ldr_values = [entry[1] for entry in ldr_data]

    return render(request, 'chartapp/index.html', {
        'temperature_labels': temperature_labels,
        'temperature_values': temperature_values,
        'humidity_labels': humidity_labels,
        'humidity_values': humidity_values,
        'rain_labels': rain_labels,
        'rain_values': rain_values,
        'ldr_labels': ldr_labels,
        'ldr_values': ldr_values,
    })
def tables_view(request):
    # Get the data for each field
    temperature_data = WeatherData.objects.all()
    humidity_data = WeatherData.objects.all()
    rain_data = WeatherData.objects.all()
    ldr_data = WeatherData.objects.all()

    return render(request, 'chartapp/tables.html', {
        'temperature_data': temperature_data,
        'humidity_data': humidity_data,
        'rain_data': rain_data,
        'ldr_data': ldr_data,
    })