from langchain.agents import initialize_agent, Tool, AgentType
from langchain_google_genai import ChatGoogleGenerativeAI
from search_tool import search_web
from scrape_tool import scrape
from typing import List

def run_agent_query(question: str, google_key: str = None) -> str:
    """
    Demonstration of an agent that can call the search and scrape tools.
    It will perform a short multi-step fetch and return combined scraped text.
    """
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=google_key, temperature=0.0)
    tools = [
        Tool(name="web_search", func=lambda q: "\n".join(search_web(q, num=5)), description="Search the web and return URLs"),
        Tool(name="web_scrape", func=lambda ucsv: str(scrape([u.strip() for u in ucsv.split(",")])), description="Scrape given URLs (comma-separated).")
    ]

    agent = initialize_agent(tools=tools, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=False)
    return agent.run(question)
