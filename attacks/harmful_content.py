from attacks.base_attack import BaseAttack


class HarmfulContentAttack(BaseAttack):

    def __init__(self):

        super().__init__(
            "datasets/harmful_content.json"
        )

    def get_attack_name(self):

        return "Harmful Content"