import requests

from src.weather_ai.api import get_weather_data


# Main entry point for the Weather AI application

def get_location() -> tuple:
    """
    Get user's current location (latitude and longitude) using IP-based geolocation.
    
    Returns:
        Tuple containing latitude and longitude
    """
    try:
        # Get user's current location (IP-based)
        ip_response = requests.get("http://ip-api.com/json/", timeout=10)
        if ip_response.status_code != 200:
            raise Exception(f"Unable to determine location. Status code: {ip_response.status_code}")
        
        location_data = ip_response.json()
        lat = location_data['lat']
        lon = location_data['lon']
        
        return (lat, lon)
    
    except Exception as e:
        print(f"Error fetching location data: {e}")
        return (None, None)


def main():
    print("Welcome to Weather AI Application")
    # Get and display location information
    lat, lon = get_location()
    if lat is not None and lon is not None:
        print(f"Latitude: {lat}")
        print(f"Longitude: {lon}")
        weather_response = get_weather_data(lat=lat, lon=lon)
        if weather_response.success:
            weather_response.data.pretty_print()
        else:
            print(f"Weather API returned {weather_response.error_message}")
    else:
        print("Failed to fetch location data")

if __name__ == "__main__":
    main()
