import json

from backend.providers.gemini import GeminiProvider


SYSTEM_PROMPT = """
You are ELVARIAN AI BUILDER CODE GENERATOR.

Your job is to convert a software project blueprint into
production-ready source code.

Return ONLY valid JSON.

Required format:

{
  "project_name": "",
  "files": [
    {
      "path": "",
      "language": "",
      "content": ""
    }
  ]
}

Rules:
- Generate complete usable files.
- Never use placeholder text such as "TODO".
- Keep the architecture consistent.
- Use secure coding practices.
- Do not expose API keys or secrets.
- Generate only files necessary for the requested project.
"""


async def generate_code(blueprint: dict):

    provider = GeminiProvider()

    prompt = f"""
{SYSTEM_PROMPT}

PROJECT BLUEPRINT:

{json.dumps(blueprint, indent=2)}
"""

    result = await provider.generate(prompt)

    try:
        return json.loads(result)

    except json.JSONDecodeError:
        return {
            "project_name": blueprint.get(
                "project_name",
                "Generated Project"
            ),
            "files": [],
            "raw_response": result
        }
