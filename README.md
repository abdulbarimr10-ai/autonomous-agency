# 🚀 Autonomous Agency
AI-Powered Competitor Intelligence System

Autonomous Agency is a multi-agent AI system that performs competitor research, strategic analysis, and content generation — enhanced with long-term vector memory and real-time Telegram alerts.

Built using FastAPI, CrewAI, Ollama, and MongoDB.

------------------------------------------------------------

🧠 WHAT IT DOES

Given a competitor URL, the system:

1. Researches the competitor using AI agents  
2. Identifies core services, target audience, and brand voice  
3. Detects strategic market gaps  
4. Generates LinkedIn positioning content  
5. Stores insights in vector memory for long-term learning  
6. Sends Telegram notifications in real-time  

------------------------------------------------------------

🏗️ ARCHITECTURE OVERVIEW

FastAPI (API Layer)
        ↓
CrewAI Multi-Agent System
        ↓
Ollama (LLM + Embeddings)
        ↓
Vector Memory (Long-Term Learning)
        ↓
MongoDB (Report Storage)
        ↓
Telegram Notifier (Monitoring)

------------------------------------------------------------

🛠️ TECH STACK

- FastAPI – Backend API  
- CrewAI – Multi-agent orchestration  
- Ollama – Local LLM + Embeddings  
- MongoDB – Report persistence  
- Vector Memory – Long-term contextual learning  
- Telegram Bot API – Execution alerts  
- Docker – Ollama container  

------------------------------------------------------------

📦 FEATURES

- Multi-agent competitive research
- Strategic gap detection
- Automated content generation
- Long-term vector memory
- Real-time Telegram notifications
- MongoDB report storage
- Dockerized LLM backend

------------------------------------------------------------

⚙️ SETUP INSTRUCTIONS

1️⃣ Clone Repository

git clone https://github.com/YOUR_USERNAME/autonomous-agency.git
cd autonomous-agency

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Setup Environment Variables

Create a file named .env in the project root:

TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
CREWAI_TRACING_ENABLED=true

4️⃣ Run Ollama (Docker)

docker run -d -p 11434:11434 --name ollama ollama/ollama
docker exec -it ollama ollama pull mistral
docker exec -it ollama ollama pull nomic-embed-text

5️⃣ Start API

uvicorn main:app --reload

Open:
http://127.0.0.1:8000/docs

------------------------------------------------------------

🔄 API USAGE

POST /analyze

Request Body:

{
  "competitor_url": "https://www.example.com/"
}

Response:

{
  "status": "completed",
  "result": { ... }
}

------------------------------------------------------------

📩 TELEGRAM ALERTS

You will receive notifications when:

- Execution starts
- Execution completes
- Error occurs

------------------------------------------------------------

🧠 VECTOR MEMORY

The system stores past competitor research embeddings to:

- Avoid repeated analysis
- Improve contextual understanding
- Enable long-term market learning

------------------------------------------------------------

📁 PROJECT STRUCTURE

autonomous-agency/
│
├── main.py
├── crew_logic.py
├── vector_memory.py
├── notifier.py
├── database.py
├── requirements.txt
├── README.md
└── .env (not committed)

------------------------------------------------------------

🚀 FUTURE IMPROVEMENTS

- Web dashboard
- Slack integration
- SaaS deployment
- Automated competitor tracking
- Scheduled intelligence reports


------------------------------------------------------------

👤 AUTHOR

Md Abdul Bari  
