# tools.py

import requests
import os
from dotenv import load_dotenv

load_dotenv()

SERPER_API_KEY = os.getenv("SERPER_API_KEY")

def serper_search(query):
    if not SERPER_API_KEY:
        raise ValueError("SERPER_API_KEY is missing in .env")

    url = "https://google.serper.dev/search"

    payload = {
        "q": query,
        "num": 5
    }

    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.json()

