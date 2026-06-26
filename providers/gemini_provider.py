from providers.base_provider import BaseProvider

class GeminiProvider(BaseProvider):

    def get_name(self) -> str:
        return "Google Gemini"

    def generate(self, prompt: str) -> str:
        raise NotImplementedError(
            "Gemini provider not connected yet."
        )