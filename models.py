from pydantic import BaseModel
from typing import List, Optional

class ResearchQuestion(BaseModel):
    question: str
    keywords: Optional[List[str]] = []
    target_domains: Optional[List[str]] = []

class ResearchPlan(BaseModel):
    topic: str
    sections: List[str]
    questions: List[ResearchQuestion]
    deliverable_outline: List[str]
