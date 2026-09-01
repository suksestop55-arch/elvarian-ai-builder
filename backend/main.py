from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os

app = FastAPI(
    title="ELVARIAN AI BUILDER",
    description="Open-source AI-powered project builder",
    version="0.1.0",
)


class ProjectRequest(BaseModel):
    prompt: str
    target: str = "web"


@app.get("/")
def root():
    return {
        "name": "ELVARIAN AI BUILDER",
        "version": "0.1.0",
        "status": "online",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/api/project/plan")
def create_project_plan(request: ProjectRequest):
    if not request.prompt.strip():
        raise HTTPException(
            status_code=400,
            detail="Project prompt cannot be empty.",
        )

    return {
        "project_prompt": request.prompt,
        "target": request.target,
        "status": "planning",
        "message": "AI project planner is ready for integration.",
    }
