import sys
import asyncio
if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
import argparse
from planner import make_plan
from search_tool import search_web
from scrape_tool import scrape
from rag import build_index, get_retriever
from writer import write_markdown
from exporter import md_to_pdf
from settings import OUTPUT_DIR
from pathlib import Path
import json

def run_research(topic: str, outdir: str = OUTPUT_DIR):
    print("1) Make plan")
    plan = make_plan(topic)
    print("Plan sections:", plan.sections)

    # 2) Search for all plan.questions
    print("2) Searching")
    urls = set()
    for q in plan.questions:
        query = q.question + " " + " ".join(q.keywords or [])
        found = search_web(query, num=6)
        for u in found:
            urls.add(u)
    urls = list(urls)[:60]
    print(f"Found {len(urls)} urls")

    # 3) Scrape
    print("3) Scraping (async)")
    scraped = scrape(urls)
    print(f"Scraped {len(scraped)} pages")

    # 4) Build index
    print("4) Building index")
    vs = build_index(scraped)

    # 5) Retrieve notes per section
    print("5) Retrieving notes")
    retriever = get_retriever(vs)
    notes = []
    for sec in plan.sections:
        docs = retriever.get_relevant_documents(sec)
        text = "\n\n".join([f"SOURCE: {d.metadata.get('source')}\n{d.page_content[:300]}" for d in docs])
        notes.append(f"## {sec}\n\n{text}")
    notes_text = "\n\n".join(notes)

    # 6) Draft
    print("6) Drafting markdown")
    md = write_markdown(plan.topic, plan.deliverable_outline, notes_text)

    # 7) Export
    out_path = Path(outdir) / (plan.topic.replace(" ", "_") + ".pdf")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    md_to_pdf(md, str(out_path))
    print("Done. PDF:", out_path)
    return {"pdf": str(out_path), "markdown": md, "plan": plan.model_dump()}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", required=True)
    args = parser.parse_args()
    run_research(args.topic)
