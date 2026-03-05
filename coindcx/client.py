import json
import httpx
import time
from config import settings
from .auth import sign_payload

BASE_URL = "https://api.coindcx.com"

async def private_post(endpoint: str, body: dict):
    # Use round() to ensure no floating point weirdness
    body["timestamp"] = int(round(time.time() * 1000))
    
    # 1. Convert to a strict, spaceless JSON string
    json_body = json.dumps(body, separators=(',', ':'))
    
    # 2. Sign the EXACT string you are about to send
    signature = sign_payload(settings.COINDCX_SECRET_KEY, json_body)

    headers = {
        "Content-Type": "application/json",
        "X-AUTH-APIKEY": settings.COINDCX_API_KEY,
        "X-AUTH-SIGNATURE": signature
    }

    async with httpx.AsyncClient() as client:
        # 3. Use 'content' instead of 'json' to send the exact string
        resp = await client.post(
            BASE_URL + endpoint,
            content=json_body, 
            headers=headers
        )
        resp.raise_for_status() # Always catch HTTP errors!
        return resp.json()