from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel

from backend.agents.project_planner import create_project_plan
from backend.agents.code_generator import generate_code


load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent


app = FastAPI(
    title="ELVARIAN AI BUILDER",
    description="Open-source AI-powered application builder",
    version="0.2.0",
)


class ProjectRequest(BaseModel):
    prompt: str
    target: str = "web"


@app.get("/")
def root():
    return {
        "name": "ELVARIAN AI BUILDER",
        "version": "0.2.0",
        "status": "online",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/api/info")
def info():
    return {
        "name": "ELVARIAN AI BUILDER",
        "version": "0.2.0",
        "features": [
            "AI Project Planning",
            "Architecture Generation",
            "File Structure Generation",
            "Development Planning",
            "AI Code Generation"
        ]
    }


@app.get("/app")
def frontend():
    return FileResponse(
        BASE_DIR / "frontend" / "index.html"
    )


@app.post("/api/project/plan")
async def project_plan(request: ProjectRequest):

    if not request.prompt.strip():
        raise HTTPException(
            status_code=400,
            detail="Project prompt cannot be empty.",
        )

    try:

        result = await create_project_plan(
            request.prompt,
            request.target,
        )

        return {
            "success": True,
            "project": result,
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error),
        )


@app.post("/api/project/code")
async def project_code(request: ProjectRequest):

    if not request.prompt.strip():
        raise HTTPException(
            status_code=400,
            detail="Project prompt cannot be empty.",
        )

    try:

        blueprint = await create_project_plan(
            request.prompt,
            request.target,
        )

        code = await generate_code(
            blueprint
        )

        return {
            "success": True,
            "project": blueprint,
            "code": code,
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error),
        )
