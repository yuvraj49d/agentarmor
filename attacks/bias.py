from attacks.base_attack import BaseAttack


class BiasAttack(BaseAttack):

    def __init__(self):

        super().__init__(
            "datasets/bias.json"
        )

    def get_attack_name(self):

        return "Bias"