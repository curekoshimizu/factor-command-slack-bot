#!/usr/bin/env python

import json

def handler(event, content):
    try:
        body = { "message": "hello" }
        status_code = 200
    except Exception as e:
        status_code = 500
        body = {"description": str(e)}
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "text/plain"
        },
        "body": json.dumps(body)
    }
