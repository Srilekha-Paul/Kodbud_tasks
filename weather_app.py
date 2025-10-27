import requests
import json

# Your actual OpenWeatherMap API key
API_KEY = "68b5ac8a30d8947d0c642d33c28b5049"

# Correct API endpoint
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    # Construct API request URL
    url = f"{BASE_URL}?q={city_name}&appid={API_KEY}&units=metric"
    
    # Send GET request
    response = requests.get(url)
    
    # Check if request was successful
    if response.status_code == 200:
        data = response.json()
        
        # Extract information
        main = data['main']
        weather = data['weather'][0]
        
        temperature = main['temp']
        humidity = main['humidity']
        condition = weather['description']
        
        # Display results
        print("\n🌤️  Weather Information 🌤️")
        print(f"City: {data['name']}")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {condition.title()}")
        print(f"Humidity: {humidity}%")
        
    else:
        print("\n❌ City not found. Please check the name and try again.")

# Main program
if __name__ == "__main__":
    print("=== Weather Now App ===")
    city = input("Enter city name: ").strip()
    get_weather(city)
