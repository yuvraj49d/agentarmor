from abc import ABC, abstractmethod


class BaseAgent(ABC):

    @abstractmethod
    def ask(self, question: str) -> str:
        pass