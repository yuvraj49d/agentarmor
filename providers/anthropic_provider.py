from clients.anthropic_client import AnthropicClient
from providers.base_provider import BaseProvider


class AnthropicProvider(BaseProvider):

    def __init__(self):

        self.client = AnthropicClient()

    def get_name(self):

        return "Anthropic Claude"

    def generate(
        self,
        prompt: str
    ) -> str:

        return self.client.generate(
            prompt
        )