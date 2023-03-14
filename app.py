import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from listeners import register_listeners
from constants import HELLO
from modalView import modalView
# from messageBlocks import blocksOfDiff
from product import oldProduct
# Initialize the app
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))


@app.shortcut("action_name_refresh")
def open_modal(ack, shortcut, client):
    # Acknowledge the shortcut request
    ack()
    # Call the views_open method using the built-in WebClient
    client.views_open(
        trigger_id=shortcut["trigger_id"],
        # A simple view payload for a modal
        view=modalView
    )


@app.view("")
def handle_submission(ack, body, client, view, logger):
    data = view["state"]["values"]["Environment"]
    user_id = body["user"]["id"]
    print(data)
    ack()
    msg = f"Hey <@{user_id}>! Your request has been submitted"
    try:
        result = client.chat_postMessage(channel="C04MRB90FUL", text=msg)
        message_id = result["ts"]
    except Exception as e:
        logger.exception(f"Failed post a message {e}")
    diff_text = str(oldProduct)
    send_diff(client, logger, message_id, diff_text)


def send_diff(client, logger, message_id, diff_text: str):
    try:
        upload_and_then_share_file = client.files_upload_v2(
        channel="C04MRB90FUL",
        thread_ts=message_id,
        title="Diff product data",
        filename="diff.json",
        content=diff_text,
        initial_comment="Here is the refresh result",
        snippet_type="json",
        ) 
        logger.info("send out the file")
    except Exception as e:
        logger.exception(f"Failed post a message {e}")



# Start the app
if __name__ == "__main__":
    register_listeners(app)
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
