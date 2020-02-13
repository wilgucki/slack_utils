import json
import os

from slack_utils.exceptions import SlackException


def verify_token(token):
    if token != os.getenv('SLACK_VERIFICATION_TOKEN'):
        raise SlackException('Invalid verification token')


def respond(challenge, token):
    verify_token(token)
    return {
        'statusCode': 200,
        'body': json.dumps({
            'challenge': challenge
        }),
        'headers': {
            'Content-Type': 'application/json'
        }
    }


# TODO write tests
