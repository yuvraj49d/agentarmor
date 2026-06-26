from providers.base_provider import BaseProvider

class OpenAIProvider(BaseProvider):

    def get_name(self) -> str:
        return "OpenAI GPT-4o"

    def generate(self, prompt: str) -> str:
        raise NotImplementedError(
            "OpenAI provider not connected yet."
        )