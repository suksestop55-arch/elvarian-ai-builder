import json

from backend.providers.gemini import GeminiProvider


SYSTEM_PROMPT = """
You are ELVARIAN AI BUILDER, an expert software architect.

Analyze the user's application idea and return a structured project plan.

Return ONLY valid JSON.

The JSON must contain:

{
  "project_name": "",
  "summary": "",
  "target": "",
  "features": [],
  "technology_stack": [],
  "architecture": [],
  "database": [],
  "api": [],
  "file_structure": [],
  "development_steps": []
}

Do not include markdown.
"""


async def create_project_plan(user_prompt: str, target: str):
    provider = GeminiProvider()

    prompt = f"""
{SYSTEM_PROMPT}

Target platform:
{target}

User project request:
{user_prompt}
"""

    result = await provider.generate(prompt)

    try:
        return json.loads(result)
    except json.JSONDecodeError:
        return {
            "project_name": "Generated Project",
            "summary": result,
            "target": target,
            "features": [],
            "technology_stack": [],
            "architecture": [],
            "database": [],
            "api": [],
            "file_structure": [],
            "development_steps": [],
        }
