import requests, json
import telebot
from telebot.handler_backends import SkipHandler as Skip
print("\n\n\tTELEGRAM WEATHER BOT")

#setting API key for telegram bot
bot=telebot.TeleBot("API KEY HERE")

@bot.message_handler(commands=['start'])
def greet(message):
    msg="Hello,"+message.chat.first_name +" "+ message.chat.last_name +", Welcome to Weather 2495 bot, The bot where you can check live weather from literally any location."
    bot.send_message(message.chat.id,msg)
    bot.send_message(message.chat.id,"Type /2495, and then start entering the city name or pincode.")

@bot.message_handler(commands=['2495'])
def weather(messge):
    @bot.message_handler(func=lambda message: True)
    def A3(messge):
        print(messge.text)
        city_name = str(messge.text)
        complete_url = "http://api.openweathermap.org/data/2.5/weather?" + "appid=" + "API KEY HERE" + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            #getting weather types (clear sky,few clouds,scattered clouds,broken clouds,shower rain, rain,thunderstorm,snow,mist)
            w_type=x['weather'][0]['main']
            print(w_type)
            text="\nLocation: "+str(x['name'])+"\nWeather: "+str(x['weather'][0]['main'])+"\nTemperature: "+ str(round(float(x['main']['temp']-273.15),2))+" °c"+"\nHumidity: "+str(x['main']['humidity'])+"%"+"\nPressure: "+str(x['main']['pressure'])+"hPa"+"\nVisibility:"+str(x['visibility'])+"m"+"\nWind speed:"+str(x['wind']['speed'])+"m/s"
            if "Rain" in w_type:
                bot.send_photo(messge.chat.id,"https://images2.imgbox.com/de/88/EeDIdDIC_o.jpg","It's raining out here man!, stay safe inside.")
            elif "Snow" in w_type:
                bot.send_photo(messge.chat.id,"https://images2.imgbox.com/19/bc/8KlfQIzq_o.jpg","Yaay!!, It's snowing here, l'm gonna build a snowman")
            elif "Mist" in w_type:
                bot.send_photo(messge.chat.id,"https://images2.imgbox.com/95/1e/bTM7ygAw_o.png","Kinda misty out here, it's a good time to plant some trees!!")
            elif "sky" or "cloud" in w_type:
                bot.send_photo(messge.chat.id,"https://images2.imgbox.com/9d/ed/dtphK5en_o.jpg","It's a clear sunny cloudy day, time to enjoy!")
            else:
                print("Exception error")
            bot.send_message(messge.chat.id,text)
        else:
            bot.send_message(messge.chat.id,"That city or place does not exit!")


bot.infinity_polling()
