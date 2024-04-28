import requests

# Welcome Screen
print("==== Weather App ====")

city = input("Enter City Name: ").title().replace(" ", "+")

# API 
response = requests.get("https://api.weatherapi.com/v1/current.json?key=bc2fda6394e24ad5a1552807240204&q=" + city)

if (response.status_code == 200):

    info = response.json()

    location = info['location']['name']
    temperature_celsius = info['current']['temp_c']
    weather_condition = info['current']['condition']['text']

    print("\n" f'Location: {location}')
    print(f'Temperature: {temperature_celsius}°C')
    print(f'Weather Condition: {weather_condition}')

else:
    if (str(response.status_code).startswith(str(4))):
        print("City not found. Please try again.")
    else:
        print(response.status_code)
        print("Internal error. Please try again later.")
