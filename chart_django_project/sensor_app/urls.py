from django.urls import path
from .views import SensorDataAPI, sensor_data_view

urlpatterns = [
    path('api/sensor_data/', SensorDataAPI.as_view(), name='sensor_data_api'),
    path('sensor_data/', sensor_data_view, name='sensor_data_view'),
]
