from django.urls import path
from .views import WeatherDetailView

urlpatterns = [
    path('weather/city/', WeatherDetailView.as_view(), name='weather-detail'),
    # другие URL-адреса вашего приложения
]
