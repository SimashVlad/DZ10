from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, ContextTypes, MessageHandler, CallbackQueryHandler, ConversationHandler, Filters

updater = Updater('5498101437:AAHNMtqhJB7DQ6IUaSQuGslg0_fxJ-yI6Xc')
dispatcher = updater.dispatcher

global n 
n = 202
global m 
m = 28
names = []
START = 0
FIRSTNAME = 1
SECONDNAME = 2
OPERATION = 3
RESULT = 4
first_name = ''
second_name = ''




# board = [[InlineKeyboardButton('Да', callback_data='0')]]
# update.message.reply_text('Попробуете?', reply_markup=InlineKeyboardMarkup(board))

def log(update: Update, context: ContextTypes):
    file = open(r'C:\Users\Начальник\Repozitorii\PYTHON\Seminar_10_DZ\ddb.csv', 'a', encoding='utf-8')
    file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}\n')
    file.close()

def start(update, context):
    log(update, context)
    context.bot.send_message(update.effective_chat.id, 'Добро пожаловать в бота, в котором '
                                                       'можно попытаться сыграть в игру 2021 конфета\n'
                                                       'Правила игры: \n1) На столе лежит 2021 конфета.' 
    'Играют два игрока, делая ход друг после друга. \n2) За один ход можно забрать не более 28 конфет.' 
    '\n3) Все конфеты оппонента достаются тому, кто сделал последний ход. \nУдачной игры!\n')
   
    context.bot.send_message(update.effective_chat.id, 'Введите имя первого человека: ')
    
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
    return OPERATION


def operation(update, context):
    log(update, context)
    global n
    global names
    names = [first_name, second_name]
    count = 1
    while n > 0:
        update.message.reply_text(f'\n{names[count % 2]}, Ваш ход: ')
        msg = int(update.message.text)
        size = msg
        update.message.reply_text(f'Осталось конфет: ')
    n = n - size
    context.bot.send_message(f'Осталось конфет = {n - size}')
    # update.effective_chat.id, 
    if n > 0:
        context.bot.send_message(update.effective_chat.id, f'Осталось конфет = {n}')
    else: 
        context.bot.send_message(update.effective_chat.id, f'Больше нет конфет')
    count += 1
    return OPERATION





def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, 'Прощай!')

    return ConversationHandler.END



start_handler = CommandHandler('start', start)
cancel_handler = CommandHandler('cancel', cancel)
nameone_handler = MessageHandler(Filters.text, first_names)
nametwo_handler = MessageHandler(Filters.text, second_names)
oper_handler = CommandHandler('oper', operation)
conv_handler = ConversationHandler(entry_points=[start_handler],
                                   states={
                                       FIRSTNAME: [nameone_handler],
                                       SECONDNAME: [nametwo_handler],
                                        OPERATION: [oper_handler],
                                   },
                                   fallbacks=[cancel_handler])


dispatcher.add_handler(conv_handler)

print('server start')
# dispatcher.add_handler(conv_handler)
updater.start_polling()
updater.idle()