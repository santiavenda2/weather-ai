# Weather data models
from typing import Optional

from pydantic import BaseModel


class WeatherData(BaseModel):
    """Structured representation of weather data from OpenWeatherMap."""

    # Main weather information
    temperature: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int

    # Weather conditions
    description: str
    main_condition: str

    # Wind information
    wind_speed: float
    wind_direction: int | None = None

    # Additional info
    visibility: int | None = None
    cloudiness: int | None = None

    # Location coordinates
    latitude: float
    longitude: float

    # Timestamp and other metadata
    timestamp: int
    location_name: str

    def pretty_print(self) -> None:
        """Print a formatted, human-readable version of the weather data."""
        print(f"Weather in {self.location_name}")
        print(f"Temperature: {self.temperature}°C (feels like {self.feels_like}°C)")
        print(f"Min/Max Temperature: {self.temp_min}°C / {self.temp_max}°C")
        print(f"Pressure: {self.pressure} hPa")
        print(f"Humidity: {self.humidity}%")
        print(f"Condition: {self.main_condition} - {self.description}")
        print(f"Wind Speed: {self.wind_speed} m/s")
        if self.wind_direction is not None:
            print(f"Wind Direction: {self.wind_direction}°")
        if self.visibility is not None:
            print(f"Visibility: {self.visibility} meters")
        if self.cloudiness is not None:
            print(f"Cloudiness: {self.cloudiness}%")
        print(f"Coordinates: {self.latitude}°, {self.longitude}°")
        print(f"Timestamp: {self.timestamp}")


class WeatherResponse(BaseModel):
    """Complete response structure for weather API."""

    data: Optional[WeatherData]
    success: bool = True
    error_message: str | None = None
