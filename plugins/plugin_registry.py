from providers.dummy_provider import DummyProvider
from attacks.prompt_injection import PromptInjectionAttack
from evaluators.security_evaluator import SecurityEvaluator
from providers.gemini_provider import GeminiProvider

class PluginRegistry:

    def __init__(self):

        self.providers = {
            "dummy": DummyProvider,
            "gemini": GeminiProvider,
        }

        self.attacks = {
            "prompt_injection": PromptInjectionAttack
        }

        self.evaluators = {
            "security": SecurityEvaluator
        }

    def get_provider(self, name):

        if name not in self.providers:
            raise ValueError(
                f"Unknown provider: {name}"
            )

        return self.providers[name]()

    def get_attack(self, name):

        if name not in self.attacks:
            raise ValueError(
                f"Unknown attack: {name}"
            )

        return self.attacks[name]()

    def get_evaluator(self, name):

        if name not in self.evaluators:
            raise ValueError(
                f"Unknown evaluator: {name}"
            )

        return self.evaluators[name]()