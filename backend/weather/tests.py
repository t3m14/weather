from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Weather  # предположим, у вас есть модель Weather для кэширования погоды

class WeatherAPITestCase(APITestCase):
    def test_get_weather_with_valid_city_name(self):
        url = reverse('weather')
        city_name = 'Moscow'
        response = self.client.get(url, {'city_name': city_name})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_weather_with_invalid_city_name(self):
        url = reverse('weather')
        city_name = 'NonExistentCity'
        response = self.client.get(url, {'city_name': city_name})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_weather_with_empty_city_name(self):
        url = reverse('weather')
        city_name = ''
        response = self.client.get(url, {'city_name': city_name})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_weather_with_numeric_city_name(self):
        url = reverse('weather')
        city_name = '1'
        response = self.client.get(url, {'city_name': city_name})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
