# database.py

import os
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime

load_dotenv(dotenv_path=".env")

client = MongoClient(os.getenv("MONGO_URI"))
db = client["autonomous_agency"]
collection = db["competitive_reports"]

def save_report(data):
    document = {
        "competitor_url": data["competitor_url"],
        "research": data["research"],
        "strategy": data["strategy"],
        "content": data["content"],
        "created_at": datetime.utcnow()
    }

    collection.insert_one(document)
    print("✅ Report saved to MongoDB")
