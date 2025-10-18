# Weather AI

A weather application that fetches data from your current location.

## Setup Instructions

To set up this project from the GitHub repository:

1. Clone the repository:
   ```bash
   git clone https://github.com/santiavenda2/weather-ai.git
   cd weather-ai
   ```

2. Install uv (if not already installed):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. Install dependencies using uv:
   ```bash
   uv sync
   ```

4. Install in development mode with editable installs:
   ```bash
   uv pip install -e .
   ```

### Adding New Dependencies

To add a new dependency:
```bash
uv pip install <package-name>
```

To add a dependency to the project's pyproject.toml:
```bash
uv pip install --group main <package-name>
```

### Running the Application

To run the application:
```bash
python src/weather_ai/main.py
```

## Getting an OpenWeatherMap API Key

To use this application, you'll need a free API key from OpenWeatherMap:

1. Visit [OpenWeatherMap](https://openweathermap.org/api)
2. Sign up for a free account
3. Navigate to your API keys section
4. Copy your API key
5. Set it as an environment variable:
   ```bash
   export OPENWEATHERMAP_API_KEY="your_actual_api_key_here"
   ```

## Project Structure

- `src/weather_ai/` - Main source code directory
- `pyproject.toml` - Project configuration and dependencies

## Running Tests

To run the tests for this project, use the following command:
```bash
uv run python -m pytest tests/
```
