from attacks.base_attack import BaseAttack


class PromptInjectionAttack(BaseAttack):

    def __init__(self):

        super().__init__(
            "datasets/prompt_injection.json"
        )

    def get_attack_name(self):

        return "Prompt Injection"