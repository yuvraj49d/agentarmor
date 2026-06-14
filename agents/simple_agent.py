from openai import OpenAI
from config.settings import OPENAI_API_KEY, MODEL_NAME

client = OpenAI(api_key=OPENAI_API_KEY)


class SimpleAgent:

    def ask(self, question: str) -> str:
        return "This is a sample response from AgentArmor."