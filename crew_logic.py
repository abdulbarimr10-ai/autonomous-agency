# crew_logic.py

from crewai import Crew
from agents import research_agent, strategy_agent, creative_agent
from tasks import create_tasks
from database import save_report
from vector_memory import store_embedding, retrieve_similar




def run_agency(competitor_url):

    past_insights = retrieve_similar(competitor_url)

    tasks = create_tasks(competitor_url)

    crew = Crew(
        agents=[research_agent, strategy_agent, creative_agent],
        tasks=tasks,
        verbose=True
    )

    result = crew.kickoff()

    print("🔥 Crew finished execution")

    report_data = {
        "competitor_url": competitor_url,
        "research": str(tasks[0].output),
        "strategy": str(tasks[1].output),
        "content": str(tasks[2].output)
    }

    print("📦 About to save:", report_data)

    save_report(report_data)

    print("✅ Save function executed")

    # 🧠 Store vector memory
    combined_text = f"""
    Research:
    {report_data['research']}

    Strategy:
    {report_data['strategy']}
    """

    store_embedding(
        combined_text,
        metadata={"competitor": competitor_url}
    )


    return report_data
