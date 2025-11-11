#Familiarize yourself with the OpenWeather weather API at: https://openweathermap.org/api. Your task is to write a program that asks the user for the name of a municipality and then prints out the corresponding weather condition description text and temperature in Celsius degrees. Take a good look at the API documentation. You must register for the service to receive the API key required for making API requests. Furthermore, find out how you can convert Kelvin degrees into Celsius.
import requests

#https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
def get_weather(api_key, city_name):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()
    weather_description = data['weather'][0]['description']
    temperature = data['main']['temp']
    return weather_description, temperature



api_key = "68d19ed4b1699b2bae65b8dd055d82ef"
city_name = input("Enter the name of a municipality: ")

weather_description, temperature = get_weather(api_key, city_name)

print(f"Weather in {city_name}: {weather_description}")
print(f"Temperature: {temperature} °C")



