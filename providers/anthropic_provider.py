from providers.base_provider import BaseProvider

class AnthropicProvider(BaseProvider):

    def get_name(self) -> str:
        return "Anthropic Claude"

    def generate(self, prompt: str) -> str:
        raise NotImplementedError(
            "Anthropic provider not connected yet."
        )