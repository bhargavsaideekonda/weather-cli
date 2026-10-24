import requests

def get_weather(latitude, longitude):
    r = requests.get("https://api.open-meteo.com/v1/forecast", params={"latitude": latitude, "longitude": longitude, "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"}, timeout= 10)
    data = r.json()
    current, units = data['current'], data["current_units"]
    return current, units
def find_city(name):
     r = requests.get("https://geocoding-api.open-meteo.com/v1/search", params={"name": name, "count": 1}, timeout=10)
     data = r.json()
     if "results" not in data:
        raise ValueError("City not found")
     real_name = data["results"][0]["name"]
     country = data["results"][0]["country"]
     latitude, longitude= (data["results"][0]["latitude"]), (data["results"][0]["longitude"])
    
     return latitude, longitude, f"{real_name}, {country}"
    
city = input("City: ")
try:
    lat, lon, place = find_city(city)
    current, units = get_weather(lat, lon)
    print(place)
    print(f"Temperature: {current['temperature_2m']} {units['temperature_2m']}")
    print(f"Humidity: {current['relative_humidity_2m']} {units['relative_humidity_2m']}")
    print(f"Wind: {current['wind_speed_10m']} {units['wind_speed_10m']}")
except ValueError:
    print("Sorry, I couldn't find that city.")
except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
    print("No internet connection. Check your Wi-Fi and try again.")