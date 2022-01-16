from aiogram.utils import executor

from bot.commands import dispatcher

if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)
