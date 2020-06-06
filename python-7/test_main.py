from main import get_temperature
import pytest

class MockResponse:
 @staticmethod
 def json():
     return {'lat': -14.235004, 'lng':-51.92528,'currently': {'temperature',62}}


def test_get_temperature_by_lat_lng():
    lat = -14.235004
    lng = -51.92528 
    expected = 16

    def mockrequest(self):
        return MockResponse()
        result = get_temperature(lat, lng)
        assert result == expected

