from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, ContextTypes, MessageHandler, CallbackQueryHandler, ConversationHandler, Filters
import datetime
from spy import *

def proverInt(update, size):
    try:
        return int(size)
    except:
        return update.message.reply_text(f'\nОшибка, введите число от 1 до 28: ')





# def bot():
#     print('Игра с ботом!')
#     player = input('Введите Ваше имя: ')
#     bot_player = 1 
#     def play_game_with_bot(n, player):
#         count = 0
#         while n > 0:
#             count = count % 2
#             if count == 1:
#                 num = randint(1, 29)
#                 print(f'\nХодит бот: {num}')
#                 n = n - num
#                 counting(n, count, player)
#             if count == 0:
#                 size = int(input(f'\n{player}, Ваш ход: '))
#                 if size > 28 or size <= 0:
#                     attempt = 3
#                     print('Ошибка!')
#                     while attempt > 0:
#                         size = int(input(f'Осталось попыток {attempt}. Введите число от 1 до 28: '))
#                         if size > 28 or size <= 0:
#                             attempt -= 1
#                         else:
#                             break
#                     if attempt == 0:
#                         return print('Вы проиграли!')
#                 n = n - size
#                 counting(n, count, player)
#             count += 1
#     play_game_with_bot(n, player)