from django.http import JsonResponse
from .models import WeatherData
from django.utils import timezone

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

