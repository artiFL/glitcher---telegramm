import telebot
import urllib3 
import logging, sys
from telebot import types, apihelper
import subprocess
from classet import argument
import classet as cl
from forfuck import main
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

#   python C:\Users\artif\Desktop\python\telegramm.py
#   this bot can
#   receive and save 
#       photo
#       video(!> 200Mb)
#       document
#   logging to .txt file
#   send random face to local(locatoin_save) and chat as site(thispersondoesnotexist.com)
admin_id =  
TOKEN = ""
locatoin_save = 'C:/Users/xxx/Desktop/bot_download/'
location_input_image = 'C:/Users/xxx/Desktop/glitch_bot/input_image/'
location_output_image = 'C:/Users/xxx/Desktop/glitch_bot/output_image/'



flagrgbshift = 0
flagstribe = 0
flaggammaset = 0
flagsq = 0
flaglt = 0
flagrp = 0

bot = telebot.TeleBot(TOKEN)

# loggoute of file 
data_list = []
def loggoute (id_add, message):
    if id_add == admin_id:
        id_add = 'admin'
    data_list.append('id        ' + str(id_add))
    data_list.append('message   ' + str(message) + '\n')
    with open (locatoin_save + 'log/log.txt', 'w+') as f:
        f.writelines("%s\n" % line for line in data_list )

# send image on site
def send_image (id):
    photo = open(argument.output, 'rb')
    bot.send_photo(id, photo)
    #if id != admin_id:
       # bot.send_photo(admin_id, photo)
    photo.close()

# treatment text handler
@bot.message_handler(content_types=["text"] )
def handle_text(message):

#"""init global variable"""
    global flagrgbshift, flagstribe, flaggammaset, flagsq, flaglt, flagrp

#"""default case handler"""
    if message.text == "/default":
        argument.rgb_kt = 12
        argument.stripe = 0
        argument.gamma = 0.3
        argument.s_quality = 3
        argument.bitrate = 10
        argument.lp = 10
        argument.rp = 95
        argument.ch_num = 0
        bot.send_message(message.from_user.id, cl.dafaultSettings)

#"""show settings case handler"""
    if message.text == "/showsettings":
        bot.send_message(message.from_user.id, "rgbshift = "+str(cl.argument.rgb_kt)+'\n'+"stripe = "+str(cl.argument.stripe)+'\n'+"gamma = " +  str(cl.argument.gamma)+'\n'+"quality = " +  str(cl.argument.s_quality)+'\n'+"lcontras = " +  str(cl.argument.lp)+'\n'+"rcontrast = " +  str(cl.argument.rp))

#"""start help case handler"""
    if message.text == "/start" or message.text == "/help" and (flagrgbshift != 0 or flagstribe != 0 or flaggammaset != 0 or flagsq != 0 or flaglt != 0 or flagrp != 0):
        flagrgbshift = 0
        flagstribe = 0
        flaggammaset = 0
        flagsq = 0
        flaglt = 0
        flagrp = 0
        bot.send_message(message.from_user.id, cl.support)

#'''help case'''
    if message.text == "/help":
        bot.send_message(message.from_user.id, cl.support)

#'''rgbshift set case'''
    if message.text != 0 and flagrgbshift != 0:
        flagrgbshift = 0
        if int(message.text) <= 0:
            bot.send_message(message.from_user.id, "l_p arg not must be < 0")
            flagrgbshift = 1
            return
        argument.rgb_kt = int(message.text)
        bot.send_message(message.from_user.id, argument.rgb_kt)

    if message.text == "/rgbshift":
        bot.send_message(message.from_user.id, "rgbshift (0 - 100)= ")
        flagrgbshift = 1

#'''stripe set case'''
    if message.text != 0 and flagstribe != 0:
        flagstribe = 0
        if int(message.text) != 1 and int(message.text) != 0:
            bot.send_message(message.from_user.id, "ты че дебил блять, тут либо 1 либо 0")
            flagstribe = 1
            return
        argument.stripe = int(message.text)
        bot.send_message(message.from_user.id, argument.stripe)

    if message.text == "/stripe":
        bot.send_message(message.from_user.id, "stripe (1 or 0) = ")
        flagstribe = 1

#'''gamma set case'''
    if message.text != 0 and flaggammaset != 0:
        flaggammaset = 0
        if float(message.text) > 0.5 or float(message.text) < 0.1:
            bot.send_message(message.from_user.id, "ты че дебил блять?")
            flaggammaset = 1
            return
        argument.gamma = float(message.text)
        bot.send_message(message.from_user.id, message.text)

    if message.text == "/gamma":
        bot.send_message(message.from_user.id, "gamma (0.1 - 0.5)= ")
        flaggammaset = 1
#'''quality set case'''
    if message.text != 0 and flagsq != 0:
        flagsq = 0
        if not 0 <= int(message.text) <= 10:
            bot.send_message(message.from_user.id, "Sound quality must be in range [0..10]!")
            flagsq = 1
            return
        argument.s_quality = int(message.text)
        bot.send_message(message.from_user.id, argument.s_quality)

    if message.text == "/quality":
        bot.send_message(message.from_user.id, "quality (0 - 5) = ")
        flagsq = 1
#'''contrast low case'''
    if message.text != 0 and flaglt != 0:
        flaglt = 0
        if not 0 <= int(message.text) <= 50:
            bot.send_message(message.from_user.id, "l_p arg must be > 0 and < 50")
            flaglt = 1
            return
        argument.lp = int(message.text)
        bot.send_message(message.from_user.id, argument.lp)

    if message.text == "/lcontrast":
        bot.send_message(message.from_user.id, "lcontrast (0 - 50) = ")
        flaglt = 1
#'''contrast high qality case'''
    if message.text != 0 and flagrp != 0:
        flagrp = 0
        if not 50 <= int(message.text) <= 100:
            bot.send_message(message.from_user.id, "l_p arg must be > 50 and < 100")
            flagrp = 1
            return
        argument.rp = int(message.text)
        bot.send_message(message.from_user.id, argument.rp)

    if message.text == "/rcontrast":
        bot.send_message(message.from_user.id, "rpontrast (50 - 100) = ")
        flagrp = 1

#''' save photo'''
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    bot.reply_to(message, "Wait")
    try:
        file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = location_input_image + file_info.file_path 
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
        argument.input = src
        argument.output = location_output_image + file_info.file_path
        main(argument)
        send_image(message.from_user.id)
    except Exception as e:
        bot.reply_to(message, "it's fiasco" + у)

# logg to consol
logger = telebot.logger
formatter = logging.Formatter('[%(asctime)s] %(thread)d {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s','%m-%d %H:%M:%S')
ch = logging.StreamHandler(sys.stdout)
logger.addHandler(ch)
logger.setLevel(logging.DEBUG)  
ch.setFormatter(formatter)

bot.polling(none_stop=True, interval=0)
