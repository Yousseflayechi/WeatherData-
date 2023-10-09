# Weather Data Retrieval Application

The Weather Data Retrieval Application is a Python program that allows users to retrieve and display weather data for a specific city using the OpenWeatherMap API. This simple application provides real-time weather information, including the country name, weather conditions, descriptions, sunrise, and sunset times.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Acknowledgments](#acknowledgments)

## Getting Started

### Prerequisites

Before using this application, you need to have the following software and libraries installed on your system:

- Python (version 3.6 or higher)
- Required Python libraries: `requests`, `tkinter`, `datetime`, `json`

You can install the necessary Python libraries using the following command:

```bash
pip install requests tkinter
```

### Installation

1. Clone this repository or download the Python script (`weather_app.py`) to your local machine.

2. Open the Python script (`weather_app.py`) in a text editor or integrated development environment (IDE).

3. Replace `"YOURKEY"` in the script with your OpenWeatherMap API key. You can obtain an API key by signing up on the [OpenWeatherMap website](https://openweathermap.org/).

## Usage

1. Run the Python script (`weather_app.py`).

2. The application's graphical user interface (GUI) will appear.

3. Enter the name of the city for which you want to retrieve weather data in the provided input field.

4. Click the "Click" button to initiate the data retrieval process.

5. The weather data, including the country name, main weather condition, description of weather, sunrise time, and sunset time, will be displayed in the text area within the GUI.


## Acknowledgments

- Special thanks to OpenWeatherMap for providing the weather data API.
- This project is open for contributions and improvements.
