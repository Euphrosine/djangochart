from django.urls import path
from . import views

urlpatterns = [
    path('chart_data/', views.chart_data_view, name='chart_data_view'),
    path('dashboard/', views.dashboard_view, name='dashboard_view'),


]
