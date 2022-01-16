"""Модуль для работы с отправкой писем."""
import smtplib, ssl
from asyncio import sleep
from email.message import EmailMessage

from bot.settings import SMTP_SERVER, SMTP_PORT, EMAIL_PASS, SENDER_EMAIL


async def send_email(receiver_email: str, text: str,
                     sender_email: str = SENDER_EMAIL,
                     subject: str = None, delay: int = 0) -> None:
    """
    Отправить сообщение на почту
    :param receiver_email: получатель, список получателей
    :param text: текст сообщения
    :param sender_email: почта отправителя
    :param subject: тема письма
    :param delay: задержка перед отправкой в секундах
    """
    await sleep(delay)
    context = ssl.create_default_context()
    msg = EmailMessage()
    msg.set_content(text)
    if subject:
        msg['Subject'] = subject
    msg['From'] = sender_email
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
        server.login(sender_email, EMAIL_PASS)
        server.send_message(msg, from_addr=sender_email, to_addrs=receiver_email)
