from langchain_google_genai import ChatGoogleGenerativeAI
from typing import List
from settings import GOOGLE_API_KEY

def write_markdown(topic: str, outline: List[str], retrieved_notes: str, llm_kwargs: dict = None) -> str:
    if llm_kwargs is None:
        llm_kwargs = {"model": "gemini-1.5-flash", "temperature": 0.0, "google_api_key": GOOGLE_API_KEY}
    llm = ChatGoogleGenerativeAI(**llm_kwargs)

    prompt = f"""
You are a precise research writer. Produce a clean Markdown report for the topic: "{topic}".
Use this outline (H2/H3 headings). For each heading, write 2-4 paragraphs or bullet points as appropriate.
Cite sources inline like [^1], [^2]. At the end include a "References" section mapping citation numbers to URLs.

Outline:
{chr(10).join(['- ' + s for s in outline])}

Notes / retrieved evidence (do not invent — use these notes):
{retrieved_notes[:20000]}

Return only Markdown.
"""
    resp = llm.invoke([("system", "You are a careful writer."), ("human", prompt)])
    md = getattr(resp, "content", str(resp))
    return md
