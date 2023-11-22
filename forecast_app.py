import json
import requests
from retrying import retry
from config import API_BASE_URL, WEATHER_API_KEY


# Function to check if the city name is valid
def is_valid_city_name(city):
    return all(char.isalpha() or char.isspace() for char in city)


# Retry decorator is used to handle transient errors during API requests
@retry(wait_exponential_multiplier=1000, wait_exponential_max=10000, stop_max_attempt_number=5)
def get_forecast(api_key, city):
    # Define the base URL of the API
    base_url = API_BASE_URL

    # Define the parameters as a dictionary
    params = {'city': city}

    # Set the API key in the headers
    headers = {'x-api-key': api_key}

    try:
        # Make the API request with the constructed URL and parameters
        response = requests.get(base_url, params=params, headers=headers)

        # Check if the response status code indicates success
        response.raise_for_status()

        # Parse the JSON data from the response
        weather_data = response.json()

        return weather_data

    except requests.exceptions.RequestException as e:
        # Handle any exceptions that might occur during the request
        print(f"Error fetching data for {city}: {e}")
        return None
    except Exception as e:
        # Catch any other unexpected exceptions
        print(f"An unexpected error occurred: {e}")
        return None


def calculate_forecast(forecast_data):
    # Extract temperatures from the forecast data
    temperatures = [entry['screenTemperature'] for entry in forecast_data]

    # Calculate the minimum and maximum temperatures
    min_temperature = min(temperatures)
    max_temperature = max(temperatures)

    return min_temperature, max_temperature


def print_results(city, min_temperature, max_temperature):
    # Display the forecast results
    print(f'Min Temperature: {min_temperature}°C')
    print(f'Max Temperature: {max_temperature}°C')
    print(f'Results for {city} saved to {city}_weather_data.json')


def save_to_json(data, filename):
    try:
        # Open the file in write mode ('w')
        with open(filename, 'w') as json_file:
            # Use the json.dump() method to write data to the file
            json.dump(data, json_file)
        # Print a success message
        print(f'Data saved to {filename} successfully.')

    except FileNotFoundError:
        # Handle the case where the specified file path is not found
        print(f'Error: The specified file path {filename} was not found.')

    except Exception as e:
        # Handle any other exceptions that might occur during file writing
        print(f'An error occurred while saving data to {filename}: {e}')


if __name__ == "__main__":
    api_key = WEATHER_API_KEY

    def get_valid_city_input():
        while True:
            user_input = input("Enter the city: ")
            if is_valid_city_name(user_input):
                print(f"City '{user_input}' is valid.")
                return user_input
            else:
                print("Invalid city name. Please enter a valid city name.")

    try:
        city = get_valid_city_input()
        weather_data = get_forecast(api_key, city)

        if weather_data and 'forecast' in weather_data:
            forecast_data = weather_data['forecast']
            min_temperature, max_temperature = calculate_forecast(forecast_data)
            print_results(city, min_temperature, max_temperature)
            data = {'city': city, 'minTemperature': min_temperature, 'maxTemperature': max_temperature}
            save_to_json(data, f'{city}_weather_data.json')
        else:
            print(f'Weather data not available for {city}')

    except Exception as e:
        print(f'An error occurred: {e}')