"""Модуль с настройками."""
# email
SMTP_PORT = 465  # For SSL
SMTP_SERVER = 'smtp.yandex.ru'
EMAIL_LOGIN = 'login'  # Логин почты до @
SENDER_EMAIL = f'{EMAIL_LOGIN}@yandex.ru'  # Enter your address
EMAIL_PASS = 'ccgdjvrxmwbxzkid'  # Пароль от почты, если 2fa включена, то от приложения

# bot
API_TOKEN = 'token'  # Токен бота сгенерированный в @BotFather
DEBUG = True
