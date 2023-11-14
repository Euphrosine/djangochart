from django.http import JsonResponse
from django.shortcuts import render,redirect
from .models import WeatherData
from django.utils import timezone
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'chartapp/register.html', {'form': form})
# https://sensor-and-chart.onrender.com/chart_data/?temperature=value&humidity=value&rain=value&ldr=value

def chart_data_view(request):
    temperature = request.GET.get('temperature', None)
    humidity = request.GET.get('humidity', None)
    rain = request.GET.get('rain', None)
    ldr = request.GET.get('ldr', None)
    moisture = request.GET.get('moisture', None)

    # Create a dictionary to store the data you want to save
    data_to_save = {
        'timestamp': timezone.now(),
        'temperature': temperature,
        'humidity': humidity,
        'rain': rain,
        'ldr': ldr,
        'moisture': moisture,
    }

    # Remove None values from the dictionary
    data_to_save = {k: v for k, v in data_to_save.items() if v is not None}

    # Create a new entry in the database using the data
    WeatherData.objects.create(**data_to_save)

    return JsonResponse({"message": "Data saved successfully"})


# @login_required
def weather_data_view(request):
    # Get the data for each field
    temperature_data = WeatherData.objects.values_list('timestamp', 'temperature')
    humidity_data = WeatherData.objects.values_list('timestamp', 'humidity')
    rain_data = WeatherData.objects.values_list('timestamp', 'rain')
    ldr_data = WeatherData.objects.values_list('timestamp', 'ldr')
    moisture_data = WeatherData.objects.values_list('timestamp', 'moisture')

    # Prepare the data in a format suitable for Chart.js
    temperature_labels = [entry[0].strftime('%H:%M:%S') for entry in temperature_data]
    temperature_values = [entry[1] for entry in temperature_data]

    humidity_labels = [entry[0].strftime('%H:%M:%S') for entry in humidity_data]
    humidity_values = [entry[1] for entry in humidity_data]

    rain_labels = [entry[0].strftime('%H:%M:%S') for entry in rain_data]
    rain_values = [entry[1] for entry in rain_data]

    ldr_labels = [entry[0].strftime('%H:%M:%S') for entry in ldr_data]
    ldr_values = [entry[1] for entry in ldr_data]

    moisture_labels = [entry[0].strftime('%H:%M:%S') for entry in moisture_data]
    moisture_values = [entry[1] for entry in moisture_data]

    return render(request, 'chartapp/index.html', {
        'temperature_labels': temperature_labels,
        'temperature_values': temperature_values,
        'humidity_labels': humidity_labels,
        'humidity_values': humidity_values,
        'rain_labels': rain_labels,
        'rain_values': rain_values,
        'ldr_labels': ldr_labels,
        'ldr_values': ldr_values,
        'moisture_labels': moisture_labels,
        'moisture_values': moisture_values,
    })
def tables_view(request):
    # Get the data for each field
    temperature_data = WeatherData.objects.all()
    humidity_data = WeatherData.objects.all()
    rain_data = WeatherData.objects.all()
    ldr_data = WeatherData.objects.all()
    moisture_data = WeatherData.objects.all()

    return render(request, 'chartapp/tables.html', {
        'temperature_data': temperature_data,
        'humidity_data': humidity_data,
        'rain_data': rain_data,
        'ldr_data': ldr_data,
        'moisture_data': moisture_data,
    })

def overall_view(request):
    weather_data = WeatherData.objects.all()
    return render(request, 'chartapp/overall.html', {'weather_data': weather_data})





def generate_pdf_report(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    # Create a PDF document
    p = canvas.Canvas(response)

    # Get the data
    temperature_data = WeatherData.objects.all()
    humidity_data = WeatherData.objects.all()
    rain_data = WeatherData.objects.all()
    ldr_data = WeatherData.objects.all()
    moisture_data = WeatherData.objects.all()
    
        # Set the font for the title
    p.setFont("Helvetica-Bold", 18)

    # Draw the title
    p.drawString(40, 800, "Sensor Data Report")

    # Add the data to the PDF
    p.setFont("Helvetica", 12)
    p.drawString(50, 800, "Temperature Data:")
    for i, data in enumerate(temperature_data):
        p.drawString(70, 780 - i*20, f"Record {i+1}: {data.timestamp}, {data.temperature}") 

    p.drawString(50, 600, "Humidity Data:")
    for i, data in enumerate(humidity_data):
        p.drawString(70, 580 - i*20, f"Record {i+1}: {data.timestamp}, {data.humidity}")

    p.drawString(50, 400, "Rain Data:")
    for i, data in enumerate(rain_data):
        p.drawString(70, 380 - i*20, f"Record {i+1}: {data.timestamp}, {data.rain}")

    p.drawString(50, 200, "LDR Data:")
    for i, data in enumerate(ldr_data):
        p.drawString(70, 180 - i*20, f"Record {i+1}: {data.timestamp}, {data.ldr}")

    p.drawString(50, 50, "Moisture Data:")
    for i, data in enumerate(moisture_data):
        p.drawString(70, 180 - i*20, f"Record {i+1}: {data.timestamp}, {data.moisture}")


    # Save the PDF
    p.showPage()
    p.save()

    return response

def generate_chart_data_report_view(request):
    sensor_data = WeatherData.objects.all()
    pdf_response = generate_pdf_report(sensor_data)
    return pdf_response
