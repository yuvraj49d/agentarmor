from providers.base_provider import BaseProvider

class OllamaProvider(BaseProvider):

    def get_name(self) -> str:
        return "Ollama"

    def generate(self, prompt: str) -> str:
        raise NotImplementedError(
            "Ollama provider not connected yet."
        )