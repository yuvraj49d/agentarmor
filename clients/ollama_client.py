import os

from dotenv import load_dotenv
import requests


load_dotenv()


class OllamaClient:

    def __init__(self):

        self.base_url = os.getenv(
            "OLLAMA_BASE_URL",
            "http://localhost:11434"
        )

        self.model = os.getenv(
            "OLLAMA_MODEL",
            "llama3.2"
        )

    def generate(
        self,
        prompt: str
    ) -> str:

        response = requests.post(

            f"{self.base_url}/api/generate",

            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            },

            timeout=120
        )

        response.raise_for_status()

        return response.json()["response"]