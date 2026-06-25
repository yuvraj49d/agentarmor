import json

from attacks.base_attack import BaseAttack


class PromptInjectionAttack(BaseAttack):

    def __init__(self):
        super().__init__(
            "datasets/prompt_injection.json"
        )

    def load_prompts(self):
        with open(self.dataset_path, "r") as file:
            return json.load(file)

    def get_attack_name(self):
        return "Prompt Injection"