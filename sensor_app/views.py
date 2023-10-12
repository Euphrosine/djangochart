from django.http import JsonResponse
from .models import SensorData
from django.utils import timezone
from django.shortcuts import render




def sensor_data_view(request):
    # Get the value of the 'status' parameter from the URL
    status = request.GET.get('status', None)

    # Initialize param2 (activity) with an empty string
    activity = ""

    if status == "1":
        activity = "Unauthorized person trying to enter the car"
    elif status == "11":
        activity = "Unknown person trying to enter the car"
    
    # Create a dictionary to store the data you want to save
    data_to_save = {
        'datetime': timezone.now(),
        'activity': activity,
        'status': status
    }

    # Create a new entry in the database using the data
    SensorData.objects.create(**data_to_save)

    # Retrieve all entries from the database
    sensor_data = SensorData.objects.all()

    # Convert the data to JSON format
    response_data = [{'datetime': entry.datetime, 'activity': entry.activity, 'status': entry.status} for entry in sensor_data]

    return JsonResponse(response_data, safe=False)

def sensor_html_view(request):
    sensor_data = SensorData.objects.all()
    return render(request, 'sensor_app/index.html', {'sensor_data': sensor_data})



from .utils import generate_sensor_data_report

def my_report_view(request):
    # Get the data you want to include in the report
    sensor_data = SensorData.objects.all()  # or some other query to get the data

    # Generate the PDF report
    pdf_response = generate_sensor_data_report(sensor_data)

    # Return the PDF response
    return pdf_response

def generate_sensor_data_report_view(request):
    sensor_data = SensorData.objects.all()
    pdf_response = generate_sensor_data_report(sensor_data)
    return pdf_response
    
