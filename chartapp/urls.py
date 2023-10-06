from django.urls import path
from . import views

urlpatterns = [
    path('chart_data/', views.chart_data_view, name='chart_data_view'),

]
