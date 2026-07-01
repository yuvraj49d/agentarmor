import os

from dotenv import load_dotenv
from anthropic import Anthropic


load_dotenv()


class AnthropicClient:

    def __init__(self):

        self.client = Anthropic(
            api_key=os.getenv("ANTHROPIC_API_KEY")
        )

        self.model = os.getenv(
            "ANTHROPIC_MODEL",
            "claude-3-5-haiku-latest"
        )

    def generate(
        self,
        prompt: str
    ) -> str:

        response = self.client.messages.create(

            model=self.model,

            max_tokens=1024,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.content[0].text