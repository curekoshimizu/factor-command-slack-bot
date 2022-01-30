# factor-command-slack-bot

## Env

Put `.env` in this root directory.

`.env` example.
```
SLACK_BOT_TOKEN=xoxb-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
SLACK_SIGNING_SECRET=YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
```


## Deploy

```
$ python -m venv .venv && source ./.venv/bin/activate && pip install -U pip
$ cdk deploy
```
