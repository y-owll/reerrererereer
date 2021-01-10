from pyowm import OWM
from pyowm.utils import config as cfg
import telebot 

config = cfg.get_default_config()
config['language'] = 'ru'
owm = OWM('1ab2252099877df239dc4150e7b5b92c', config)
bot = telebot.TeleBot("1559680922:AAEDw_YF1gt_STWz9zjSTAyse3AdWfPnr5U")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place( message.text )

    w = observation.weather
    temp = w.temperature('celsius')["temp"]

    answer = "в городе " + str(message.text) + " сейчас:" + w.detailed_status + "\n"
    answer += "температура сейчас в районе:" + str(temp) + "\n\n"
    if temp < 10:
 	    answer += "суперхолодно,одевайся тепло дурачек"
    elif temp < 20:
 	    answer +=  "сейчас прохладно,одевайся потеплее"
    elif temp > 20:
	    answer += "сейчас тепло,шортики на ножки,футболочку надел и пошел иметь всех дам"

    bot.reply_to(message, answer)

bot.polling() 