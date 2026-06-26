from abc import ABC, abstractmethod

class BaseProvider(ABC):

    @abstractmethod
    def get_name(self) -> str:
        """Return provider name."""
        pass

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """Generate a response."""
        pass