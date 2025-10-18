# API module for weather data retrieval
import os
import requests
from ..models.weather import WeatherData, WeatherResponse


def get_weather_data(lat: float, lon: float) -> WeatherResponse:
    """
    Fetch current weather data for given coordinates.
    
    Args:
        lat (float): Latitude of the location
        lon (float): Longitude of the location
    
    Returns:
        Dictionary containing structured weather information
    """
    try:
        # Using OpenWeatherMap API as an example
        api_key = os.environ.get("OPENWEATHERMAP_API_KEY")  # Load from environment variables
        if not api_key:
            raise Exception("OPENWEATHERMAP_API_KEY environment variable not set")
        url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
        
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            raise Exception(f"API request failed with status code: {response.status_code}")
            
        raw_data = response.json()
        
        # Extract and structure the data
        weather_data = WeatherData(
            temperature=raw_data['main']['temp'],
            feels_like=raw_data['main']['feels_like'],
            temp_min=raw_data['main']['temp_min'],
            temp_max=raw_data['main']['temp_max'],
            pressure=raw_data['main']['pressure'],
            humidity=raw_data['main']['humidity'],
            description=raw_data['weather'][0]['description'],
            main_condition=raw_data['weather'][0]['main'],
            wind_speed=raw_data['wind']['speed'],
            wind_direction=raw_data.get('wind', {}).get('deg'),
            visibility=raw_data.get('visibility'),
            cloudiness=raw_data.get('clouds', {}).get('all'),
            latitude=lat,
            longitude=lon,
            timestamp=raw_data['dt'],
            location_name=raw_data.get('name', 'Unknown Location')
        )
        
        return WeatherResponse(data=weather_data)
    
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return WeatherResponse(success=False, error_message=str(e))


def get_current_weather() -> WeatherResponse:
    """
    Get current weather for the user's location.
    
    Returns:
        Dictionary containing structured weather information for current location
    """
    # Import here to avoid circular imports
    from ..main import get_location
    
    lat, lon = get_location()
    
    if lat is None or lon is None:
        print("Unable to determine location")
        return WeatherResponse(success=False, error_message="Location could not be determined")
        
    return get_weather_data(lat, lon)
