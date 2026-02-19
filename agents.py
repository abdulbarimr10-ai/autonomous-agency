# agents.py

from crewai import Agent,LLM
from langchain_ollama import ChatOllama   # ✅ FIXED IMPORT
from crewai.tools import tool
from tools import serper_search

# -----------------------------
# Ollama LLM (Correct Provider)
# -----------------------------
local_llm = LLM(
    model="ollama/mistral:latest",   # 👈 IMPORTANT
    api_base="http://localhost:11434",
    temperature=0.7,
    force_tool_usage=False, # 🔥 IMPORTANT
        function_calling=False   # 👈 THIS STOPS TOOL AUTO-CALL

)


# -----------------------------
# Serper Tool
# -----------------------------
@tool
def google_search(query: str):
    """Search Google for competitor information"""
    return serper_search(query)

# -----------------------------
# Research Agent
# -----------------------------
research_agent = Agent(
    role="Competitive Intelligence Researcher",
    goal="Find competitor services and brand positioning.",
    backstory="You gather information using search tools and summarize clearly.",
    tools=[google_search],
    verbose=True,
    allow_delegation=False,
    llm=local_llm,
    max_iter=3   # 👈 prevents infinite tool loops
)


# -----------------------------
# Strategy Agent
# -----------------------------
strategy_agent = Agent(
    role="Market Strategy Analyst",
    goal="Identify competitive gaps.",
    backstory="You analyze markets deeply.",
    verbose=True,
    allow_delegation=False,
    llm=local_llm
)

# -----------------------------
# Creative Agent
# -----------------------------
creative_agent = Agent(
    role="LinkedIn Content Strategist",
    goal="Write high-performing LinkedIn posts.",
    backstory="You write professional B2B content.",
    verbose=True,
    allow_delegation=False,
    llm=local_llm
)
