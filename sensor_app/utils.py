# utils.py

from reportlab.pdfgen import canvas
from datetime import datetime
from django.http import HttpResponse

def generate_sensor_data_report(sensor_data):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=sensor_data_report_{datetime.now().strftime("%Y-%m-%d_%H-%M")}.pdf'

    p = canvas.Canvas(response)

    p.setFont("Helvetica", 12)  # Set font size to 12 points

    for i, data in enumerate(sensor_data):
        y_offset = 780 - i*90  # Increase the vertical spacing between entries
    
        # Entry Label
        p.drawString(70, y_offset, f"Entry {i+1}:")

        # Data Fields
        p.drawString(90, y_offset - 20, f"DateTime: {data.datetime}")
        p.drawString(90, y_offset - 40, f"Activity: {data.activity}")
        p.drawString(90, y_offset - 60, f"Status: {data.status}")

    p.showPage()
    p.save()

    return response
