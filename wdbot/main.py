
from _config import TOKEN
import telebot
import logging


logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

bot = telebot.TeleBot(TOKEN)


contexts = {}


def menu(message):
    bot.send_message(message.chat.id, """Я могу рассказать:
    как стать самозанятым
    как получить работу
    какая есть работа для вас
    свежие новости
    об обучающих курсах и программах
    """)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Здравствуйте! Я чат-бот Юрий")
    menu(message)


@bot.message_handler(regexp='умеешь')
def how_join_message(message):
    menu(message)


@bot.message_handler(regexp='стать самозанятым')
def how_join_message(message):
    bot.send_message(message.chat.id, """
Для регистрации через приложение:
- скачать приложение «Мой налог»- https://lknpd.nalog.ru/auth/login;
- указать номер мобильного телефона;
- выбрать регион;
- добавить фото паспорта гражданина;
- сфотографировать лицо;
- подтвердить свои данные.
""")


@bot.message_handler(regexp='получить работу')
def get_job_message(message):
    bot.send_message(message.chat.id, """
У нас слишком много разных предложений. Заполните ваш профиль на сайте mb31.ru https://www.figma.com/proto/BL4vqB0OuErN6vqWmLGdOG/%D0%9B%D0%B5%D0%BD%D0%B4%D0%BE%D1%81?page-id=0%3A1&node-id=15%3A84&viewport=241%2C48%2C0.22&scaling=min-zoom&starting-point-node-id=2%3A2
""")


@bot.message_handler(regexp='работа для меня|предложения')
def for_me_job_message(message):
    bot.send_message(message.chat.id, """
На образовательный портал skyeng требуются преподаватели по вашему профилю. Регистрируемся? - https://teach.skyeng.ru/ 
""")


@bot.message_handler(regexp='новости')
def news_message(message):
    bot.send_message(message.chat.id, """Пока нет.""")


@bot.message_handler(regexp='курсы')
def courses_message(message):
    bot.send_message(message.chat.id, """Чему вы хотите научиться?
Продажи
Маркетинг
Бухгалтерия
Получить специальность
""")


@bot.message_handler(regexp='продажи')
def courses_message(message):
    bot.send_message(message.chat.id, """Мы можем предложить:
Как усилить УТП? 3 эффективных приема
Как продать (почти) любой проект инвестору: финальная формула презентации и секреты работы с осторожными инвесторами
Бесплатный вебинар: Как увеличить продажи оптовой компании с помощью CRM
""")


@bot.message_handler(regexp='консультаци')
def consult_message(message):
    bot.send_message(message.chat.id, """
    Для записи на онлайн консультацию нужно перейти \
    по ссылке https://helponline.mfc31.ru/citizen/claims/new?department_id=14 \
    и выбрать удобные дату и время.
""")


@bot.message_handler(regexp='^(да|ага|угу|yes|yep|(yes )?of course|конечно)')
def yes_message(message):
    global contexts
    yes = contexts.get(('yes', message.chat.id))
    if yes == 'what i can':
        menu(message)
        del contexts[('yes', message.chat.id)]
    else:
        bot.send_message(message.chat.id, """Чтото я запутался о чем мы. Хотите расскажу, что я умею?""")
        contexts[('yes', message.chat.id)] = 'what i can'


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, """Я пока не умею отвечать на такие фразы, но я быстро обучаюсь.
В ближайшее время я научусь отвечать на ваш вопрос. Хотите узнать, что я уже умею?""")
    contexts[('yes', message.chat.id)] = 'what i can'


if __name__ == '__main__':
    bot.infinity_polling()
