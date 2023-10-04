from django.urls import path
from .views import SensorDataAPI, sensor_data_view

urlpatterns = [
    path('api/sensor_data/', SensorDataAPI.as_view(), name='sensor_data_api'),
    path('api/sensor_data/<int:status_code>/', SensorDataAPI.as_view(), name='sensor_data_api_status'),
    path('sensor_data/', sensor_data_view, name='sensor_data_view'),
]
