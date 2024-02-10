from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import get_weather_from_yandex

class WeatherDetailView(APIView):
    CACHE_TIMEOUT = 1800  # Время жизни кеша в секундах (в данном случае 30 минут)

    def get(self, request, format=None):
        city_name = str(request.query_params.get('city'))
        if not city_name or city_name.is_numeric() or city_name == '':
            return Response({'error': 'City name is required'}, status=status.HTTP_400_BAD_REQUEST)
        cache_key = f'weather_{city_name}'
        cached_data = cache.get(cache_key)

        if cached_data:
            # Если данные есть в кеше, возвращаем их
            return Response(cached_data)
        else:
            # Если данных нет в кеше, получаем их из API и кешируем
            weather_data = get_weather_from_yandex(city_name)
            if not weather_data:
                return Response({'error': 'City not found'}, status=status.HTTP_404_NOT_FOUND)
            cache.set(cache_key, weather_data, self.CACHE_TIMEOUT)
            return Response(weather_data)
