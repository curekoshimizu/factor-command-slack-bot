import os
from slack_bolt import App
from slack_bolt.adapter.aws_lambda import SlackRequestHandler
from sympy.ntheory import factorint


app = App(process_before_response=True,
    token=os.environ["SLACK_BOT_TOKEN"], 
    signing_secret=os.environ["SLACK_SIGNING_SECRET"]
)


def _prime_factorization(n):
    ret_message = f"{n} = "
    try:
        is_first_element = True
        d = factorint(n)
        assert len(d) > 0
        for p in sorted(d.keys()):
            count = d[p]
            while count > 0:
                if is_first_element:
                    ret_message += str(p)
                    is_first_element = False
                else:
                    ret_message += f" * {p}"
                count -= 1
    except Exception:
        ret_message = f"{n} is invalid argument."
    return ret_message


@app.event("app_mention")
def handle_mention(body, say, logger):
    user = body["event"]["user"]
    message = body["event"]["text"]
    for text in reversed(message.split(" ")):
        try:
            n = int(text)
            break
        except Exception:
            pass
    else:
        say("Invalid message")

    ret_message = _prime_factorization(n)
    say(f"<@{user}> {ret_message}")

def handler(event, context):
    slack_handler = SlackRequestHandler(app=app)
    return slack_handler.handle(event, context)
