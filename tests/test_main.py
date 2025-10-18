import pytest
from unittest.mock import patch, Mock
from src.weather_ai.main import get_location


def test_get_location_success():
    """Test successful location retrieval"""
    # Mock the requests.get response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "lat": 40.7128,
        "lon": -74.0060
    }
    
    with patch('src.weather_ai.main.requests.get', return_value=mock_response):
        lat, lon = get_location()
        
        assert lat == 40.7128
        assert lon == -74.0060


def test_get_location_api_failure():
    """Test location retrieval when API returns error"""
    # Mock the requests.get response with a non-200 status code
    mock_response = Mock()
    mock_response.status_code = 500
    mock_response.json.return_value = {}
    
    with patch('src.weather_ai.main.requests.get', return_value=mock_response):
        lat, lon = get_location()
        
        assert lat is None
        assert lon is None


def test_get_location_exception():
    """Test location retrieval when an exception occurs"""
    with patch('src.weather_ai.main.requests.get', side_effect=Exception("Network error")):
        lat, lon = get_location()
        
        assert lat is None
        assert lon is None
