# tools/ollama_tool.py

from crewai.tools import BaseTool
import requests
import os

class OllamaTool(BaseTool):
    name: str = "OllamaTool"
    description: str = "Ferramenta que usa o modelo LLM local via Ollama"

    def _run(self, input: str) -> str:
        model = os.getenv("OPENAI_MODEL_NAME", "llama3")
        try:
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={"model": model, "prompt": input, "stream": False}
            )
            response.raise_for_status()
            return response.json().get("response", "").strip()
        except Exception as e:
            return f"[Erro ao chamar Ollama]: {e}"
