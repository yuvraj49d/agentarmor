from attacks.base_attack import BaseAttack


class RoleOverrideAttack(BaseAttack):

    def __init__(self):

        super().__init__(
            "datasets/role_override.json"
        )

    def get_attack_name(self):

        return "Role Override"