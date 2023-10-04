from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SensorData
from datetime import datetime
from django.shortcuts import render
from .models import SensorData

class SensorDataAPI(APIView):
    def post(self, request):
        # Assuming you receive 'status' in the request data
        status_code = request.data.get('status', 0)
        
        if status_code == 1:
            activity = "Unauthorized person trying to enter the car"
        elif status_code == 11:
            activity = "Unknown person trying to enter in the car"
        else:
            activity = "No activity"
            
        SensorData.objects.create(datetime=datetime.now(), activity=activity)
        return Response({'message': 'Data recieved successfully'}, status=status.HTTP_201_CREATED)



def sensor_data_view(request):
    sensor_data = SensorData.objects.all()
    return render(request, 'sensor_app/sensor_data.html', {'sensor_data': sensor_data})