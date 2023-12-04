import telebot as t
import datetime as dt
import time

bot = t.TeleBot('')
mk = {}
registr = {}
registr1 = {'Аня': 954736914, 'nik': 334649449, 'Лилия': 1204249471, 'katerina': 868771919, 'Настя': 1049350446, 'Оля': 1374780831, 'Maria': 5271640028}
otvet = {}
itog1 = {}

@bot.message_handler(commands=['PROVERKA'])
def start(message):
    x = message.id
    y = message.chat.id
    print(message.chat.id)
    bot.delete_message(y, x)

@bot.message_handler(commands=['MK'])
def start(message):
    your = message.from_user.id
    x = message.id
    y = message.chat.id
    sent = bot.send_message(your, 'Пожалуйста, введите мастер класс:')
    bot.delete_message(y, x)
    bot.register_next_step_handler(sent, obr)


def obr(message):
    MK = message.text
    name1 = message.from_user.first_name
    if name1 not in mk:
        mk[name1] = MK
    else:
        mk[name1] = MK
    your = message.from_user.id
    bot.send_message(your, 'Мастер-класс зарегистрирован')
    print(mk)

@bot.message_handler(commands=['MK1'])
def pros(message):
    x = message.id
    y = message.chat.id
    your = message.from_user.id
    bot.delete_message(y, x)
    for i in mk:
        bot.send_message(your, f'{i} ведет {mk[i]}')

@bot.message_handler(commands=['REGISTR'])
def finals(message):
    user_id = message.from_user.id
    name47 = message.from_user.first_name
    x = message.id
    y = message.chat.id
    bot.delete_message(y, x)
    if name47 not in registr:
        registr[name47] = user_id
    bot.send_message(user_id, 'Вы зарегитрированы в нашем боте')
    print(registr)

@bot.message_handler(commands=['OPROS'])
def opros(message):
    x = message.id
    y = message.chat.id
    bot.delete_message(y, x)
    for i in registr1:
        n = registr1[i]
        sent = bot.send_message(n, '<b><i>ДЕЖУРНЫЙ ЗАПРОСИЛ У ВАС ИНФОРМАЦИЮ</i></b>\n\nOтветьте ему \n\n<i>Cколько у Вас детей?</i>, <i>Какой у Вас мастер-класс?</i> <i>И где вы?</i> \n\n<b>ПРИМЕР:</b>\n\n<b>6 Футбол Спортзал\n\n(!ПЕРВЫМ! указывать ЧИСЛО детей)</b>', parse_mode='HTML')
        bot.send_photo(n, open(r'C:\Users\NikNik\Desktop\V\v8.jpg', 'rb'))
        bot.register_next_step_handler(sent, obr2)

def obr2(message):
    x47 = message.text
    y47 = message.from_user.first_name
    your47 = message.from_user.id

    its = x47.split()
    if its[0].isdigit() and len(its) >= 3:
        bot.send_message(your47,f'Дежурный принял ответ')
        otvet[y47] = x47
        print(otvet)

    else:
        bot.send_photo(your47, open(r'C:\Users\NikNik\Desktop\V\v9.jpg', 'rb'))
        sent = bot.send_message(your47,'<b><i>ДЕЖУРНЫЙ ЗАПРОСИЛ У ВАС ИНФОРМАЦИЮ</i></b>\n\nOтветьте ему \n\n<i>Cколько у Вас детей?</i>, <i>Какой у Вас мастер-класс?</i> <i>И где вы?</i> \n\n<b>ПРИМЕР:</b>\n\n<b>6 Футбол Спортзал\n\n(!ПЕРВЫМ! указывать ЧИСЛО детей)</b>',parse_mode='HTML')
        bot.register_next_step_handler(sent, obr2)
        bot.send_photo(your47, open(r'C:\Users\NikNik\Desktop\V\v8.jpg', 'rb'))

@bot.message_handler(commands=['CHET'])
def chet(message):
    sums = 0
    z47 = message.from_user.id
    id3 = message.id
    x = message.id
    y = message.chat.id
    bot.delete_message(y, x)
    for i in registr1:
        if i not in otvet:
            otvet[i] = 'пользователь не ответил'
    for i in otvet:
        if otvet[i] == 'пользователь не ответил':
            sums += 0
        else:
            c47 = otvet[i].split()
            print(int(c47[0]))
            sums += int(c47[0])

    bot.send_message(z47, f'Сейчас занято {sums} детей')
    for i in otvet:
        bot.send_message(z47, f'{i} : {otvet[i]}')

bot.polling()