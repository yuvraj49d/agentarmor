from clients.ollama_client import OllamaClient
from providers.base_provider import BaseProvider


class OllamaProvider(BaseProvider):

    def __init__(self):

        self.client = OllamaClient()

    def get_name(self):

        return "Ollama"

    def generate(
        self,
        prompt: str
    ) -> str:

        return self.client.generate(
            prompt
        )