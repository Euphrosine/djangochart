from django.urls import path
from .views import sensor_data_view,sensor_html_view,my_report_view,generate_sensor_data_report_view


urlpatterns = [
    # ... your other URL patterns ...
    path('sensor_view/', sensor_html_view, name='sensor_view'),
    path('sensor_data/', sensor_data_view, name='sensor_data_view'),
    path('generate_report/', my_report_view, name='generate_report'), 
    path('generate_sensor_data_report/', generate_sensor_data_report_view, name='generate_sensor_data_report'),
]
