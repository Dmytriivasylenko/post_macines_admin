import unittest
from unittest.mock import patch
from flask import Flask
from app import app, get_coordinates, get_weather_data, API_KEY, GOOGLE_MAPS_API_KEY


class TestWeatherApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('app.get_coordinates')
    @patch('app.get_weather_data')
    def test_successful_weather_request(self, mock_get_weather_data, mock_get_coordinates):
        mock_get_coordinates.return_value = {'lat': 50.45, 'lon': 30.52}

        mock_get_weather_data.return_value = {
            'latitude': 50.45,
            'longitude': 30.52,
            'temperature': 20,
            'wind_speed': 5,
            'precipitation': 0,
            'location': "Lat: 50.45, Lon: 30.52"
        }

        response = self.app.post('/weather', data={'location': 'Kyiv'})

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Lat: 50.45, Lon: 30.52', response.data)
        self.assertIn(b'Temperature', response.data)
        self.assertIn(GOOGLE_MAPS_API_KEY.encode(), response.data)

    @patch('app.get_coordinates')
    def test_unsuccessful_geocoding(self, mock_get_coordinates):
        mock_get_coordinates.return_value = None

        response = self.app.post('/weather', data={'location': 'Unknown City'})

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Error: Could not retrieve weather data for the specified location.', response.data)

    @patch('app.get_coordinates')
    @patch('app.requests.get')
    def test_unsuccessful_weather_data(self, mock_requests_get, mock_get_coordinates):
        mock_get_coordinates.return_value = {'lat': 50.45, 'lon': 30.52}
        mock_requests_get.side_effect = Exception("Weather API error")
        response = self.app.post('/weather', data={'location': 'Kyiv'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Error: Could not retrieve weather data for the specified location.', response.data)

    @patch('app.requests.get')
    def test_get_coordinates_success(self, mock_requests_get):
        mock_requests_get.return_value.json.return_value = [
            {'lat': 50.45, 'lon': 30.52}
        ]

        result = get_coordinates('Kyiv')
        self.assertEqual(result, {'lat': 50.45, 'lon': 30.52})
        mock_requests_get.assert_called_with(
            'http://api.openweathermap.org/geo/1.0/direct',
            params={'q': 'Kyiv', 'appid': API_KEY}
        )

    @patch('app.requests.get')
    def test_get_weather_data_success(self, mock_requests_get):
        mock_requests_get.return_value.json.return_value = {
            'current': {
                'temp': 20,
                'wind_speed': 5,
                'rain': {'1h': 0}
            }
        }

        result = get_weather_data({'lat': 50.45, 'lon': 30.52})
        self.assertEqual(result, {
            'latitude': 50.45,
            'longitude': 30.52,
            'temperature': 20,
            'wind_speed': 5,
            'precipitation': 0,
            'location': "Lat: 50.45, Lon: 30.52"
        })

        mock_requests_get.assert_called_with(
            'https://api.openweathermap.org/data/3.0/onecall',
            params={
                'lat': 50.45,
                'lon': 30.52,
                'appid': API_KEY,
                'units': 'metric'
            }
        )



if __name__ == '__main__':
    unittest.main()
