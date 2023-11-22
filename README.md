# Pre-Interview Exercise - Weather Forecast App
<h4> - Lauren Southall </h4>



## About:
<p>The Weather Forecast App is a console application designed to provide users with historical weather data for a specified city. Users can input the name of a city, and the application queries a forecast API to retrieve historical weather data. The app then calculates and displays the minimum and maximum temperatures for each day in the dataset. The results are saved locally in a JSON-formatted file for future reference</p>

## Installation Instructions:

**1. Clone the Repository:**

<ul><h6>  Clone the repository containing the Weather Forecast App (WFA) to your local machine.</h6>

  `git clone <repository_url>`</ul>
     
**2. Navigate to the App Directory:**

<ul><h6>Change your working directory to the location where the WFA code is saved.</h6>

`cd path/to/weather-forecast-app`</ul>

**3. Install Dependencies:**
<ul><h6>Install the required dependencies using pip. Run the following command:</h6>

`pip install requests retrying`</ul>

**4. Provide API Key:**

<ul><h6>Open the ‘config.py’ file and replace the placeholder ‘WEATHER_API_KEY’ with your own API key. Save the file.</h6></ul>


**5. Run the Application:**

<ul><h6>Execute the ‘forecast_app.py’ file using the following command:</h6>

`python forecast_app.py`</ul>

**6. Enter City Name:**

<ul><h6>When prompted, enter the name of the city for which you want to retrieve historical weather data.</h6></ul>


**7. View Results:**

<ul><h6>The app will display the minimum and maximum temperatures for each day and the results will be saved to a JSON file.</h6></ul>


**8. Check JSON File:**

<ul><h6>Open the generated JSON file (_e.g., ‘London_weather_data.json’_) to view the saved weather data.</h6></ul>


## Useful Links:

<ul>Link to Python installation:
  https://www.python.org/downloads/
</ul>

<ul>Link to Weather API:
https://openweathermap.org/api</ul>
