from django.contrib import admin
from django.urls import path, include
from chartapp.views import generate_pdf_report


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chartapp.urls')),
    path('api/', include('sensor_app.urls')),
    path('generate_report/', generate_pdf_report, name='generate_pdf_report'),  
]

