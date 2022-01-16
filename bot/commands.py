"""Модуль с коммандами."""
import re
from datetime import timedelta, datetime
from random import randrange

from aiogram import Bot, Dispatcher, types

from bot.mailer import send_email
from bot.settings import API_TOKEN, DEBUG

bot = Bot(token=API_TOKEN)
dispatcher = Dispatcher(bot)


@dispatcher.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message) -> None:
    """Отправить приветственный текст / помощь."""
    text = '''
    Привет, я бот для отправки писем. Вот что я умею:\n
    /send <текст письма> -r <email1, email2> -t <Тема письма> -w <now|later> 
    - команда для отправки сообщения
    '''
    await message.reply(text)


@dispatcher.message_handler(commands=['send'])
async def execute_send_command(message: types.Message) -> None:
    """Выполнить команду по отправке сообщения с обработкой ошибки."""
    try:
        await send_mail_command(message)
    except Exception as err:
        msg = err if DEBUG else 'Что то пошло не так, проверьте правильность команды.'
        await message.reply(msg)


async def send_mail_command(message: types.Message) -> None:
    """Выполнить команду по отправке сообщения."""
    flags = 't|r|w'  # список флагов
    _, raw_message = message.get_full_command()
    msg = re.match(r'(.+?)(?= -\w)', raw_message).group()
    key_val = re.split(fr' -({flags}) ', raw_message.replace(msg, ''))[1:]
    args = dict(zip(key_val[::2], key_val[1::2]))

    delay = 0
    if args.get('w', 'now') != 'now':
        till_end_day = datetime.now().replace(hour=0, minute=0, second=0) + timedelta(days=1) - datetime.now()
        max_delay = int(till_end_day.total_seconds())
        delay = randrange(1, max_delay)
        await message.reply(
            f'Готово. Письмо будет отправлено через {timedelta(seconds=delay)}')
    else:
        await message.reply('Готово')
    await send_email(args['r'].split(', '), msg, subject=args.get('t'), delay=delay)
