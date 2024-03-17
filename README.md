Hello!!

RUNS ONLY ON PYTHON VERSION 3.9 AND ABOVE

So within the zip file, there is four .py files.

By default you would need the following module
 	requests and json (they are builtin functions in python)

1.api_backend.py is the normal python code which gets weather data and prints to console

2.weather_gui.py is the code for a micro app. It requires the following modules to be installed
    $ pip install PyMsgBox

3.telegram_bot.py is the code for telegram bot (https://t.me/weather_2495_bot). It requires the following modules to be installed
    $ pip install pyTelegramBotAPI

4. sample_api_out.py is a sample code to show what kind of data is sent by the weather api


For more context, in this project we are using openweathermap.org's api, which is free 
and provides worldwide weather data.
