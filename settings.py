import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

CHROMA_PERSIST_DIR = os.getenv("CHROMA_PERSIST_DIR", "data/chroma")
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "data/output")

Path(CHROMA_PERSIST_DIR).mkdir(parents=True, exist_ok=True)
Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

# Basic validation
if not GOOGLE_API_KEY:
    print("Warning: GOOGLE_API_KEY (or GEMINI_API_KEY) not set. Gemini API calls will fail.")
if not SERPAPI_API_KEY:
    print("Warning: SERPAPI_API_KEY not set. Search will fail.")
