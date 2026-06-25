from abc import ABC, abstractmethod


class BaseAttack(ABC):
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        
    @abstractmethod
    def load_prompts(self):
        pass

    @abstractmethod
    def get_attack_name(self):
        pass