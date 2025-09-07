# from serpapi.google_search_results import GoogleSearch
# from settings import SERPAPI_API_KEY

# def search_web(query: str, num: int = 6) -> list:
#     """
#     Returns a list of high-quality URLs for the query using SerpAPI.
#     """
#     if not SERPAPI_API_KEY:
#         raise RuntimeError("SERPAPI_API_KEY not set in environment")

#     params = {
#         "engine": "google",
#         "q": query,
#         "api_key": SERPAPI_API_KEY,
#         "num": num
#     }
#     search = GoogleSearch(params)
#     results = search.get_dict()
#     urls = []
#     # SerpApi places results in 'organic_results' typically
#     for r in results.get("organic_results", [])[:num]:
#         link = r.get("link") or r.get("url")
#         if link:
#             urls.append(link)
#     return urls

from serpapi.google_search import GoogleSearch
from settings import SERPAPI_API_KEY


def search_web(query: str, num: int = 6) -> list:
    """
    Returns a list of high-quality URLs for the query using SerpAPI.
    """
    if not SERPAPI_API_KEY:
        raise RuntimeError("SERPAPI_API_KEY not set in environment")

    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_API_KEY,
        "num": num
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    urls = []

    # SerpApi places results in 'organic_results' typically
    for r in results.get("organic_results", [])[:num]:
        link = r.get("link") or r.get("url")
        if link:
            urls.append(link)

    return urls
