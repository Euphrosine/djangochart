from django.urls import path
from .views import sensor_data_view,sensor_html_view

urlpatterns = [
    # ... your other URL patterns ...
    path('sensor_view/', sensor_html_view, name='sensor_view'),
    path('sensor_data/', sensor_data_view, name='sensor_data_view'),
]
