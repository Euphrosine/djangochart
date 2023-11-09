from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('chart_data/', views.chart_data_view, name='chart_data_view'),
    path('', views.overall_view, name='overall_page'),
    path('charts/', views.weather_data_view, name='charts_page'),
    path('tables/', views.tables_view, name='tables_page'),
    path('register/', views.register, name='register'),
    path('login/', auth_view.LoginView.as_view(template_name='chartapp/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='chartapp/logout.html'), name="logout"),

]
