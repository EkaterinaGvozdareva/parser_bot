import requests
from bs4 import BeautifulSoup
import random
import telebot

URL = 'https://www.anekdot.ru/last/good/'
token = '5584640169:AAHhPLTT_50SrA0anMoADFWo-YXL-5qDc5M'


def parser(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [i.text for i in anekdots]


list_of_jokes = parser(URL)
random.shuffle(list_of_jokes)

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, 'Привет! Чтобы получить анекдот напишите "анекдот"')


@bot.message_handler(content_types=['text'])
def jokes(message):
    if message.text.lower() == 'анекдот':
        bot.send_message(message.chat.id, list_of_jokes[0])
        del list_of_jokes[0]
    else:
        bot.send_message(message.chat.id, 'Чтобы получить анекдот напишите "анекдот"')


bot.polling()  # Постоянное обновление бота
