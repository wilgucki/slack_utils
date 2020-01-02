import hashlib
import hmac
from datetime import datetime

from slack_utils.signature import verify


def test_verify_request():
    timestamp = datetime.now().timestamp()
    body = 'some_body'
    slack_signing_secret = 'secret'

    base_string = f'v0:{timestamp}:{body}'
    hashed_string = 'v0=' + hmac.new(
        slack_signing_secret.encode(),
        msg=base_string.encode(),
        digestmod=hashlib.sha256
    ).hexdigest()

    assert verify(hashed_string, timestamp, body, slack_signing_secret)
