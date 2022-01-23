"""Модуль с настройками."""
# email
SMTP_PORT = 465  # For SSL
SMTP_SERVER = 'smtp.yandex.ru'
EMAIL_LOGIN = 'galynovms'  # Логин почты до @
SENDER_EMAIL = f'{EMAIL_LOGIN}@yandex.ru'  # Enter your address
EMAIL_PASS = 'NeF0rM@+'  # Пароль от почты, если 2fa включена, то от приложения

# bot
API_TOKEN = '5194984370:AAGwuNEDAhu6ziTT1HrsVMz8jaqIaee2seg'  # Токен бота сгенерированный в @BotFather
DEBUG = True
