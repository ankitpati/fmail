#!/usr/bin/env python3
"""Celery Task Queue for FMail."""

from os.path import basename
from smtplib import SMTP
from email.message import EmailMessage

from celery import Celery

ME = basename(__file__)
if ME.endswith('.py'):
    ME = ME.split('.')[:-1]

APP = Celery(ME, broker='amqp://localhost')

MAILER = SMTP('localhost')
SENDER = 'celery@localhost'


@APP.task
def sendmail(to_addr, subject, body):
    """Send email to given address."""

    msg = EmailMessage()
    msg['From'] = SENDER
    msg['To'] = to_addr
    msg['Subject'] = subject
    msg.add_alternative(body, subtype='html')

    MAILER.send_message(msg)
