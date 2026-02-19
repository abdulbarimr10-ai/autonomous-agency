# tasks.py

from crewai import Task
from agents import research_agent, strategy_agent, creative_agent


def create_tasks(competitor_url,past_memory=None):

    # -----------------------------------------
    # TASK 1: Research Competitor
    # -----------------------------------------
    research_task = Task(
        description=f"""
        Use the google_search tool to research this competitor website:

        {competitor_url}

        Your job:
        1. Identify the top 3 core services.
        2. Identify their target audience.
        3. Describe their brand voice (technical, bold, friendly, corporate, etc).

        IMPORTANT:
        - Use the search tool.
        - Base your answer on real information.
        - Provide structured output.
        """,
        agent=research_agent,
        expected_output="Plain text structured research summary.",
        tools=[research_agent.tools[0]] 
    )

    # -----------------------------------------
    # TASK 2: Strategic Analysis
    # -----------------------------------------
    strategy_task = Task(
        description="""
        Based on the research findings:

         Previous similar market insights:
    {past_memory}

        1. Identify one major competitive gap.
        2. Explain why this gap is a strategic opportunity.
        3. Suggest a positioning advantage to exploit it.

        Avoid repeating previous strategies if possible.
        Be specific and non-generic.
        """,
        agent=strategy_agent,
        expected_output="Clear market gap analysis with reasoning."
    )

    # -----------------------------------------
    # TASK 3: Creative Content
    # -----------------------------------------
    creative_task = Task(
        description="""
        Using the identified strategic gap:

        Write 3 LinkedIn posts that:
        - Start with a strong hook
        - Highlight the opportunity
        - Position us as innovative
        - Include a clear CTA

        Make them professional and engaging.
        """,
        agent=creative_agent,
        expected_output="Three polished LinkedIn posts."
    )

    # -----------------------------------------
    # TASK CHAINING (VERY IMPORTANT)
    # -----------------------------------------
    strategy_task.context = [research_task]
    creative_task.context = [strategy_task]

    return [research_task, strategy_task, creative_task]
