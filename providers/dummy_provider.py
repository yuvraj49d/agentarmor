from providers.base_provider import BaseProvider

class DummyProvider(BaseProvider):

    def get_name(self) -> str:
        return "Dummy Provider"

    def generate(self, prompt: str) -> str:

        return (
            f"Dummy response generated for: {prompt}"
        )