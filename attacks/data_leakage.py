# attacks/data_leakage.py

from attacks.base_attack import BaseAttack


class DataLeakageAttack(BaseAttack):

    def __init__(self):

        super().__init__(
            "datasets/data_leakage.json"
        )

    def get_attack_name(self):

        return "Data Leakage"