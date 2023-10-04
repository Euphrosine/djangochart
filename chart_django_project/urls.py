from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chartapp.urls')),
    path('api/', include('sensor_app.urls'))
]

