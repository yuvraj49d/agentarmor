import json

from attacks.base_attack import BaseAttack


class SystemPromptLeakageAttack(BaseAttack):

    def __init__(self):
        super().__init__(
            "datasets/system_prompt_leakage.json"
        )

    def load_prompts(self):
        with open(self.dataset_path, "r") as file:
            return json.load(file)

    def get_attack_name(self):
        return "System Prompt Leakage"