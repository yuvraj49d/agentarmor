from attacks.data_leakage import DataLeakageAttack
from attacks.role_override import RoleOverrideAttack
from providers.dummy_provider import DummyProvider
from attacks.prompt_injection import PromptInjectionAttack
from evaluators.security_evaluator import SecurityEvaluator
from providers.gemini_provider import GeminiProvider
from attacks.system_prompt_leakage import SystemPromptLeakageAttack
from attacks.jailbreak import JailbreakAttack
from providers.openai_provider import OpenAIProvider
from providers.ollama_provider import OllamaProvider
from providers.anthropic_provider import AnthropicProvider
from attacks.harmful_content import HarmfulContentAttack
from attacks.bias import BiasAttack

class PluginRegistry:

    def __init__(self):

        self.providers = {
            "dummy": DummyProvider,
            "gemini": GeminiProvider,
            "openai": OpenAIProvider,
            "ollama": OllamaProvider,
            "anthropic": AnthropicProvider,
        }

        self.attacks = {
            "prompt_injection": PromptInjectionAttack,
            "jailbreak": JailbreakAttack,
            "system_prompt_leakage": SystemPromptLeakageAttack,
            "harmful_content": HarmfulContentAttack,
            "bias": BiasAttack,
            "data_leakage": DataLeakageAttack,
            "role_override": RoleOverrideAttack
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