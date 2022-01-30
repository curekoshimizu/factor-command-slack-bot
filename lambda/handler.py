import os
from slack_bolt import App
from slack_bolt.adapter.aws_lambda import SlackRequestHandler
import time


app = App(process_before_response=True,
    token=os.environ["SLACK_BOT_TOKEN"],
    signing_secret=os.environ["SLACK_SIGNING_SECRET"]
)


@app.message("hello")
def message_hello(message, say):
    # イベントがトリガーされたチャンネルへ say() でメッセージを送信します
    say(
        blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": "こんにちは！"},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text":"ボタンを押す"},
                    "action_id": "button_click"
                }
            }
        ],
        text=f"Hey there <@{message['user']}>!"
    )

def action_button_click(body,ack,say):
    time.sleep(3)
    say("ボタンおして、3秒経過したよ！")

def demo1(body,ack,say):
    say("ボタン押したよ！")
    ack("ボタン！")

app.action("button_click")(
    ack=demo1,
    lazy=[action_button_click]
)


def handler(event, context):
    slack_handler = SlackRequestHandler(app=app)
    return slack_handler.handle(event, context)
