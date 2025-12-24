from pydantic import BaseModel
from typing import List, Dict

class ScanResponse(BaseModel):
    risk_level: str
    risk_score: int
    flags: List[Dict]
    recommendations: List[str]
