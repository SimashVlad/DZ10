from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, ContextTypes, MessageHandler, CallbackQueryHandler, ConversationHandler, Filters
import datetime
from spy import *

n = 202
names = []
count = 1
START = 0
FIRSTNAME = 1
SECONDNAME = 2
OPERATION = 3
SECONDOPERATION = 4
RESULT = 5
first_name = ''
second_name = ''


def start(update: Update, context: ContextTypes):
    log(update, context)
    context.bot.send_message(update.effective_chat.id, 'Добро пожаловать в бота, в котором '
                                                       'можно попытаться сыграть в игру 2021 конфета\n'
                                                       'Правила игры: \n1) На столе лежит 2021 конфета.' 
                                                       'Играют два игрока, делая ход друг после друга. \n2) За один ход '
                                                       'можно забрать не более 28 конфет.' 
                                                       '\n3) Все конфеты оппонента достаются тому, кто сделал последний ход. '
                                                       '\nУдачной игры!\n')
    context.bot.send_message(update.effective_chat.id, 'Введите имя первого игрока: ')
    
    return FIRSTNAME

def first_names(update, context):
    log(update, context)
    global first_name
    first_name = update.message.text
    context.bot.send_message(update.effective_chat.id, 'Отлично!\nВведите имя второго игрока: ')

    return SECONDNAME

def second_names(update, context):
    log(update, context)
    global second_name
    second_name = update.message.text
    update.message.reply_text(f'Ходит {first_name}: ')
    return SECONDOPERATION

# def numbers(number):
#         int(number)

def ostatok(update, n):
    if n != 0:
        return update.message.reply_text(f'Осталось конфет:  {n}')
    else:
        if count == 0:
            update.message.reply_text(f'Поздравляем! Побеждает {second_name}!\n{first_name}, '
                                        'не расстраивайтесь, в следующий раз у Вас обязательно получится выиграть :)')
            update.message.reply_text('Спасибо, что использовали нашего бота, ведь мы очень старались писать это чудо! Йоу!')
        else:
            update.message.reply_text(f'Поздравляем! Побеждает {first_name}!\n{second_name}, '
                                        'не расстраивайтесь, в следующий раз у Вас обязательно получится выиграть :)')
            update.message.reply_text('Спасибо, что использовали нашего бота, ведь мы очень старались!')

def proverInt(update, size):
    try:
        return int(size)
    except:
        return update.message.reply_text(f'\nОшибка, введите число от 1 до 28: ')

def first_operation(update, context):
    log(update, context)
    global n
    global names
    global size
    global count
    count = 0
    size = proverInt(update, update.message.text)
    if 0 < size and size <= 28 and size <= n:
        n = n - size
        ostatok(update, n)
        if n >= 1: 
            update.message.reply_text(f'\n{first_name}, Ваш ход: ')
            return SECONDOPERATION
        else:
            return RESULT
    else:
        if n >= 28:
            update.message.reply_text(f'\nОшибка, введите число в диапозоне 1 до 28: ')
        else:
            update.message.reply_text(f'\nОшибка, введите число в диапозоне 1 до {n}: ')

def second_operation(update, context):
    log(update, context)
    global n
    global names
    global size
    global count
    count = 1
    size = proverInt(update, update.message.text)
    if 0 < size and size <= 28 and size <= n:
        n = n - size
        ostatok(update, n)
        if n >= 1: 
            update.message.reply_text(f'\n{second_name}, Ваш ход: ')
            return OPERATION
        else:
            return RESULT
    else: 
        if n >= 28:
            update.message.reply_text(f'\nОшибка, введите число в диапозоне 1 до 28: ')
        else:
            update.message.reply_text(f'\nОшибка, введите число в диапозоне 1 до {n}: ')