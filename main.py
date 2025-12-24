from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware

from app.scoring import calculate_risk
from app.recommendations import generate_recommendations
from app.schemas import ScanResponse

app = FastAPI(title="AdGuard AI Compliance Engine")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/scan", response_model=ScanResponse)
async def scan_creative(
    file: UploadFile,
    headline: str = Form(...),
    primary_text: str = Form(...),
    description: str = Form(""),
    category: str = Form("general")
):
    combined_text = f"{headline} {primary_text} {description}"

    risk_level, risk_score, flags = calculate_risk(
        combined_text,
        category
    )

    recommendations = generate_recommendations(flags)

    return {
        "risk_level": risk_level,
        "risk_score": risk_score,
        "flags": flags,
        "recommendations": recommendations
    }
