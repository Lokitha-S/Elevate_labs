import requests
import json

def fetch_weather_data():
    # 1. Using a free public API (Open-Meteo for weather)
    url = "https://api.open-meteo.com/v1/forecast?latitude=12.97&longitude=77.59&current_weather=true"
    
    try:
        # 2. Send GET request
        response = requests.get(url)
        
        # 3. Inspect status code (200 is Success)
        if response.status_code == 200:
            # 4. Parse JSON into Python dictionary
            data = response.json()
            
            # 5. Extract fields from nested JSON
            current = data['current_weather']
            temp = current['temperature']
            wind = current['windspeed']
            
            output = f"--- Bengaluru Weather ---\nTemperature: {temp}°C\nWind Speed: {wind} km/h\n"
            
            # 6. Display clean output
            print(output)
            
            # 7. Store fetched data in a local file
            with open("weather_report.txt", "w") as file:
                file.write(output)
                print("Data saved to weather_report.txt")
        else:
            print(f"API Error: Received status code {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        # 8. Handle API errors gracefully
        print(f"Connection Error: {e}")

if __name__ == "__main__":
    fetch_weather_data()