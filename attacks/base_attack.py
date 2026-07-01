from abc import ABC, abstractmethod
import json


class BaseAttack(ABC):

    def __init__(self, dataset_path):

        self.dataset_path = dataset_path

    def load_prompts(self):

        with open(
            self.dataset_path,
            "r"
        ) as file:

            return json.load(file)

    @abstractmethod
    def get_attack_name(self):

        pass

    def get_category(self):

        return self.get_attack_name()