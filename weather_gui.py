import requests, json
import pymsgbox as mb

api_key = "api_key"
owm_url = "http://api.openweathermap.org/data/2.5/weather?"


city_name = mb.prompt("Enter the city name or pincode","Micro Weather App","eg:'chennai' or '600020'")

complete_url = owm_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url)

#contains all data recieved from API
x = response.json()

# "404", means city is not found otherwise,
if x["cod"] != "404":
    
    current_location=x['name']
    current_temperature = x["main"]["temp"]
    current_pressure = x["main"]["pressure"]
    current_humidity = x["main"]["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]
 
    # printing the values
    m="Location:"+str(current_location)+"\nTemperature (in celcius) = " +str(round(float(current_temperature-273.15),2)) +"\n atmospheric pressure (in hPa unit) = " + str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidity) +"\n description = " + str(weather_description)
    mb.confirm(m,'Micro Weather App')


else: mb.confirm(" City Not Found ",'Micro Weather APP')