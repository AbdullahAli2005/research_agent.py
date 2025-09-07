import asyncio
import httpx
import re
from selectolax.parser import HTMLParser
from tenacity import retry, wait_exponential, stop_after_attempt

USER_AGENT = "ResearchAgent/1.0 (+https://example.com)"

@retry(wait=wait_exponential(min=1, max=10), stop=stop_after_attempt(3))
async def fetch(client: httpx.AsyncClient, url: str, timeout=20):
    r = await client.get(url, headers={"User-Agent": USER_AGENT}, timeout=timeout)
    r.raise_for_status()
    return r.text

def clean_html(html: str, max_chars: int = 100_000) -> str:
    doc = HTMLParser(html)
    for sel in ["script", "style", "noscript", "header", "footer", "nav", "aside"]:
        for n in doc.css(sel):
            try:
                n.decompose()
            except Exception:
                pass
    text = doc.text(separator=" ", strip=True)
    text = re.sub(r"\s+", " ", text)
    return text[:max_chars]

async def scrape_many(urls: list[str]) -> list[dict]:
    results = []
    async with httpx.AsyncClient(follow_redirects=True) as client:
        tasks = [fetch(client, u) for u in urls]
        pages = await asyncio.gather(*tasks, return_exceptions=True)
    for u, p in zip(urls, pages):
        if isinstance(p, Exception):
            continue
        txt = clean_html(p)
        results.append({"url": u, "text": txt})
    return results

def scrape(urls: list[str]) -> list[dict]:
    return asyncio.run(scrape_many(urls))
