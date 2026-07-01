from clients.openai_client import OpenAIClient
from providers.base_provider import BaseProvider


class OpenAIProvider(BaseProvider):

    def __init__(self):

        self.client = OpenAIClient()

    def get_name(self):

        return "OpenAI"

    def generate(
        self,
        prompt: str
    ) -> str:

        return self.client.generate(
            prompt
        )