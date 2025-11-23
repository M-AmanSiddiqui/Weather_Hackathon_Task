import pandas as pd
from api_client.weather_api import get_weather

def weather_etl(city, api_key, temp_unit="C", wind_unit="m/s", pressure_unit="hPa"):
    """
    Extract → Transform → Load with unit conversions.
    
    temp_unit: "C" or "F"
    wind_unit: "m/s" or "km/h"
    pressure_unit: "hPa" or "atm"
    """
    data = get_weather(city, api_key)
    
    # Temperature conversion
    temp_c = data["main"]["temp"]
    if temp_unit.upper() == "F":
        temp = temp_c * 9/5 + 32
        temp_label = "Temperature (°F)"
    else:
        temp = temp_c
        temp_label = "Temperature (°C)"
    
    # Pressure conversion
    pressure_hpa = data["main"]["pressure"]
    if pressure_unit.lower() == "atm":
        pressure = pressure_hpa / 1013.25
        pressure_label = "Pressure (atm)"
    else:
        pressure = pressure_hpa
        pressure_label = "Pressure (hPa)"
    
    # Wind speed conversion
    wind_speed = data["wind"]["speed"]
    if wind_unit.lower() == "km/h":
        wind_speed = wind_speed * 3.6
        wind_label = "Wind Speed (km/h)"
    else:
        wind_label = "Wind Speed (m/s)"
    
    df = pd.DataFrame({
        "Parameter": [temp_label, "Humidity (%)", pressure_label, wind_label],
        "Value": [temp, data["main"]["humidity"], pressure, wind_speed]
    })
    
    return df

