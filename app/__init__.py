from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
import os

app = Flask(__name__)
Bootstrap(app)
mail = Mail()

app.jinja_env.auto_reload = True

app.config.update( SECRET_KEY = 'secret_key',
                    MAIL_SERVER = 'smtp.gmail.com',
                    MAIL_PORT = 587,
                    MAIL_USE_TLS = True,
                    MAIL_USE_SSL = False,
                    MAIL_USERNAME = 'shoppinator1.0@gmail.com',
                    MAIL_PASSWORD = 'shoppinator123!',
                    MAIL_DEFAULT_SENDER = 'info@shoppinator.com')

from datetime import datetime

def time_ago(time=False):
    """
    Get a datetime object or a int() Epoch timestamp and return a
    pretty string like 'an hour ago', 'Yesterday', '3 months ago',
    'just now', etc
    """
    now = datetime.now()
    if type(time) is int:
        diff = now - datetime.fromtimestamp(time)
    elif isinstance(time,datetime):
        diff = now - time
    elif not time:
        diff = now - now
    second_diff = diff.seconds
    day_diff = diff.days

    if day_diff < 0:
        return ''

    if day_diff == 0:
        if second_diff < 5:
            return "just now"
        if second_diff < 60:
            return str(second_diff) + " seconds ago"
        if second_diff < 120:
            return "a minute ago"
        if second_diff < 3600:
            return str(second_diff // 60) + " minutes ago"
        if second_diff < 7200:
            return "an hour ago"
        if second_diff < 86400:
            return str(second_diff // 3600) + " hours ago"
    if day_diff == 1:
        return "yesterday"
    if day_diff < 7:
        return str(day_diff) + " days ago"
    if day_diff < 14:
        return "a week ago" 
    if day_diff < 31:
        return str(day_diff // 7) + " weeks ago"
    if day_diff < 62:
        return "a month ago"
    if day_diff < 365:
        return str(day_diff // 30) + " months ago"
    if day_diff < 730:
        return "a year ago"
    return str(day_diff // 365) + " years ago"

app.jinja_env.filters['time_ago'] = time_ago

from app import views
