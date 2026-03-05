import hmac
import hashlib
import json

def sign_payload(secret: str, body: dict) -> str:
    payload = json.dumps(body, separators=(",", ":"))
    return hmac.new(
        secret.encode(),
        payload.encode(),
        hashlib.sha256
    ).hexdigest()