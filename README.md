# 📑 Research & Report Agent

An **Agentic AI project** that automates research: given a topic, it plans → searches → scrapes → organizes → and outputs a **well‑structured PDF report**.
This project uses **Gemini API**, **SerpAPI**, **LangChain**, and **FastAPI**.

---

## 🚀 Features

* Generate research reports from a single input topic
* Multi‑step autonomous pipeline:

  1. **Plan** → break topic into sections & guiding questions
  2. **Search** → gather sources via SerpAPI
  3. **Scrape** → extract content from web pages
  4. **Index** → build embeddings with Gemini API
  5. **Retrieve** → collect relevant notes for each section
  6. **Draft** → structure into markdown
  7. **Export** → save as **PDF**
* Run via **CLI** or **Web API (FastAPI)**
* Async scraping for speed
* Supports ChromaDB vector storage

---

## 📂 Project Structure

```
research_agent/
│── run.py              # CLI entrypoint
│── app.py              # FastAPI server
│── planner.py          # Creates research plan
│── search_tool.py      # Searches web using SerpAPI
│── scrape_tool.py      # Scrapes content (async)
│── rag.py              # Build embeddings & retriever
│── writer.py           # Drafts report markdown
│── exporter.py         # Converts markdown → PDF
│── settings.py         # API keys & configuration
│── requirements.txt    # Dependencies
│── README.md           # Project documentation
```

---

## ⚙️ Setup

### 1. Clone repository

```bash
git clone https://github.com/yourname/research_agent.git
cd research_agent
```

### 2. Create virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
# OR
source .venv/bin/activate  # Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set environment variables

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
SERPAPI_API_KEY=your_serpapi_api_key_here
OUTPUT_DIR=outputs
```

Get your keys:

* **Gemini API** → [Google AI Studio](https://aistudio.google.com/) → API key
* **SerpAPI** → [https://serpapi.com/](https://serpapi.com/) → API key

---

## ▶️ Usage

### Run via CLI

```bash
python run.py --topic "Quantum Computing"
```

This will:

* Generate a plan
* Search & scrape sources
* Build index & retrieve notes
* Draft markdown
* Export PDF into `outputs/`

### Run via Web API

Start the server:

```bash
uvicorn app:app --reload
```

Open docs in browser → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Endpoints:

* **POST** `/run` → Input `{ "topic": "Quantum Computing" }` → Generates report
* **GET** `/download/{filename}` → Download the generated PDF

---

## 📦 Requirements

* Python 3.9+
* [LangChain](https://www.langchain.com/)
* [SerpAPI](https://serpapi.com/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [ChromaDB](https://www.trychroma.com/)
* [Google Generative AI SDK](https://ai.google.dev/)

Install everything:

```bash
pip install -r requirements.txt
```

---

## 🛠️ Example Workflow

```bash
python run.py --topic "History of Artificial Intelligence"
```

Output:

* **outputs/History\_of\_Artificial\_Intelligence.pdf**
* Markdown draft
* Plan JSON

---

## 🔮 Future Improvements

* Add caching to avoid repeated scraping
* Integrate n8n for automation
* Add UI dashboard
* Improve summarization quality

---

## ✨ Author

Made by **Abdullah Ali** 👨‍💻

---

## 📜 License

MIT License. Use freely with attribution.
