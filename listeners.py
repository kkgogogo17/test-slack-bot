from slack_bolt import App 
from constants import HELLO

def message_hello(message, say) -> None:
    say(f"Hey there <@{message['user']}>!")



def register_listeners(app: App):
    app.message(HELLO)(message_hello) 
