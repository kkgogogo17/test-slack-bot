from app import app
from constants import HELLO
def message_hello(message, say):
    say(f"Hey there <@{message['user']}>!")



def register_listeners(app):
    app.message(HELLO)(message_hello) 
    