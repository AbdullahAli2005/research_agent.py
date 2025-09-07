import json
from langchain_google_genai import ChatGoogleGenerativeAI
from models import ResearchPlan
from settings import GOOGLE_API_KEY

def make_plan(topic: str, llm_kwargs: dict = None) -> ResearchPlan:
    """
    Uses Gemini via LangChain to produce a JSON research plan for `topic`.
    Returns a validated ResearchPlan.
    """
    if llm_kwargs is None:
        llm_kwargs = {"model": "gemini-1.5-flash", "temperature": 0.0, "google_api_key": GOOGLE_API_KEY}

    llm = ChatGoogleGenerativeAI(**llm_kwargs)

    prompt = f"""
You are a meticulous research planner. Return valid JSON only that matches this schema:
{{"topic": str,
 "sections": ["list of 6-9 section titles"],
 "questions": [{{"question": str, "keywords": ["..."], "target_domains": ["optional domain hints"]}}],
 "deliverable_outline": ["H2/H3 headings for final report"]
}}
Topic: {topic}

Produce:
- 6-9 sections
- 8-12 questions
- An outline suitable for a 6–10 page report
Return only JSON.
"""

    # Gemini via langchain returns an AIMessage with .content
    resp = llm.invoke([("system", "You are a JSON-only assistant."), ("human", prompt)])
    text = getattr(resp, "content", str(resp))

    # Defensive: if the model added explanation, try to extract JSON block
    try:
        # try direct parse
        data = json.loads(text)
    except Exception:
        # find first { ... } block
        import re
        m = re.search(r"\{.*\}", text, re.S)
        if not m:
            raise ValueError("Planner did not return JSON. Raw output:\n" + text)
        data = json.loads(m.group(0))

    plan = ResearchPlan.parse_obj(data)
    return plan
