from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SensorData
from datetime import datetime
from django.shortcuts import render
from .models import SensorData


class SensorDataAPI(APIView):


    def get(self, request):
        data = SensorData.objects.all()
        response_data = [{'datetime': entry.datetime, 'activity': entry.activity, 'status': entry.status} for entry in data]
        return Response(response_data)
    pass

    def post(self, request, status_code=None):
        if status_code is not None:
            status_code = int(status_code)

            if status_code == 1:
                activity = "Unauthorized person trying to enter the car"
            elif status_code == 11:
                activity = "Unknown person trying to enter in the car"
            else:
                activity = "No activity"

            SensorData.objects.create(datetime=datetime.now(), activity=activity)
            return Response({'message': 'Data received successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Invalid status code'}, status=status.HTTP_400_BAD_REQUEST)


def sensor_data_view(request):
    sensor_data = SensorData.objects.all()
    return render(request, 'sensor_app/sensor_data.html', {'sensor_data': sensor_data})
