x={
    'coord': {'lon': 80.2785, 'lat': 13.0878}, 
    'weather': [{'id': 701, 'main': 'Mist', 'description': 'mist', 'icon': '50n'}], 
    'base': 'stations', 
    'main': {'temp': 299.8, 'feels_like': 299.8, 'temp_min': 299.14, 'temp_max': 299.8, 'pressure': 1016, 'humidity': 88}, 
    'visibility': 5000,
    'wind': {'speed': 2.06, 'deg': 50},
    'clouds': {'all': 75}, 
    'dt': 1701352022, 
    'sys': {'type': 2, 'id': 2012809, 'country': 'IN', 'sunrise': 1701305095, 'sunset': 1701346207}, 
    'timezone': 19800, 'id': 1264527,
    'name': 'Chennai',
    'cod': 200}

print("descrpition:",x['weather'][0]['main'])
print("City:",x['name'])
print("temprature:",x['main']['temp'])
print('pressure:',x['main']['pressure'])
print('humidity:',x['main']['humidity'])
print("visibility",x['visibility'])
print("wind speed:",x['wind']['speed'])




