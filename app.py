from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from run import run_research
from fastapi.responses import FileResponse
from settings import OUTPUT_DIR
from pathlib import Path

app = FastAPI(title="Research & Report Agent")

class TopicBody(BaseModel):
    topic: str

@app.post("/run")
def post_run(body: TopicBody):
    try:
        result = run_research(body.topic)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"pdf": result["pdf"]}

@app.get("/download/{filename}")
def download_file(filename: str):
    p = Path(OUTPUT_DIR) / filename
    if not p.exists():
        raise HTTPException(status_code=404, detail="Not found")
    return FileResponse(p, media_type="application/pdf", filename=filename)
