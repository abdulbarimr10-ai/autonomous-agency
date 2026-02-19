from fastapi import FastAPI
from pydantic import BaseModel
from crew_logic import run_agency
from notifier import send_telegram_message

app = FastAPI()

class RequestData(BaseModel):
    competitor_url: str

@app.post("/analyze")
async def analyze(data: RequestData):
    try:
        # 🚀 Notify Start
        send_telegram_message(
            f"🚀 *Crew Started*\nCompetitor: {data.competitor_url}"
        )

        result = run_agency(data.competitor_url)

        # ✅ Notify Success
        send_telegram_message(
            f"✅ *Crew Completed Successfully*\nCompetitor: {data.competitor_url}"
        )

        return {"status": "completed", "result": result}

    except Exception as e:
        # ❌ Notify Error
        send_telegram_message(
            f"❌ *Crew Failed*\nError: {str(e)}"
        )

        return {"error": str(e)}
