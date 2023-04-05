import telebot
import telegram

# set the Telegram Bot API token provided by BotFather
TOKEN = '6147019965:AAEnRpWt6SrO5dLGQWy6oK-1txQkIX7yqAc'

# create a Telebot object
bot = telebot.TeleBot(TOKEN)

# define a function for the /start command
@bot.message_handler(commands=['start'])
def start(message):
    start_text = 'hello! Welcome to private server bot chat \nType /help for more info'
    bot.reply_to(message,start_text)

# define a function for the /help command
@bot.message_handler(commands=['help'])
def help(message):
    help_text = "Available commands:\n\n" \
                "/start - Start the bot\n" \
                "/files - Show available files\n" \
                "/about - Show information about the bot"
    bot.reply_to(message, help_text)
@bot.message_handler(commands=['about'])
def about(message):
    about_text= "this group is just for information purpose only \n stay safe stay healthy Make sure you subsribe psgenshin_ youtube channel"
    bot.reply_to(message,about_text)
# define a function for the /files command
# define a function for the /file command
# @bot.message_handler(commands=['files'])
# def files(message):
#     file_text = "Available files:\n\n" \
#                 "/grass - for grasscutter tools\n" \
#                 "/char - character builder tools\n" \
#                 "/allc - for all command list"
#     bot.reply_to(message, file_text)

@bot.message_handler(commands=['files'])
def files(message):
    files_text = "Available Files: \n\n"\
                 "/grasstool - for grasscutter tools\n" \
                 "/charbuild - character builder tools\n" \
                 "/allcode - for all command list"
    bot.reply_to(message,files_text)    
@bot.message_handler(commands=['grasstool'])
def send_file(message):
    # open the file you want to send
    file = open('D:/coding/project_files/GrasscutterTools-v1.8.0.exe', 'rb')
    # send the file to the user
    bot.send_document(message.chat.id, file)
    # close the file
    file.close()

@bot.message_handler(commands=['charbuild'])
def send_file(message):
    # open the file you want to send
    file = open('D:/coding/project_files/CharacterBuilder.jar','rb')
    # send the file to the user
    bot.send_document(message.chat.id, file)
    # close the file
    file.close()

@bot.message_handler(commands=['allcode'])
def send_file(message):
    # open the file you want to send
    file = open('D:/coding/project_files/handbook.txt','rb')
    # send the file to the user
    bot.send_document(message.chat.id, file)
    # close the file
    file.close()

# define a function for the /about command
@bot.message_handler(commands=['about'])
def about(message):
    about_text = "This bot was created by [your name here]. It is powered by Python and the telebot library."
    bot.reply_to(message, about_text)

# define a function for handling text messages
@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, message.text)

# start the bot
bot.polling()