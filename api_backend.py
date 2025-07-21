import requests, json

api_key = "ed93ae29452d595e94713149fda26810"
owm_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter city name : ")
complete_url = owm_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url)

#contains all data recieved from API
x = response.json()

# "404", means city is not found otherwise,
if x["cod"] != "404":
    # key in variable y
    y = x["main"]
    current_temperature = y["temp"]
    current_pressure = y["pressure"]
    current_humidity = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]
 
    # printing the values
    print(" Temperature (in kelvin unit) = " +
                    str(current_temperature) +
          "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          "\n humidity (in percentage) = " +
                    str(current_humidity) +
          "\n description = " +
                    str(weather_description))
 
else: print(" City Not Found ")