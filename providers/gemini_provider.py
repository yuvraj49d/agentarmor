from providers.base_provider import BaseProvider
from clients.gemini_client import GeminiClient


class GeminiProvider(BaseProvider):

    def __init__(self):

        self.client = GeminiClient()

    def get_name(self):

        return "Google Gemini"

    def generate(self, prompt):

        return self.client.generate(prompt)