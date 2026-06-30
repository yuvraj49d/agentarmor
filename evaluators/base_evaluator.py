from abc import ABC, abstractmethod


class BaseEvaluator(ABC):

    @abstractmethod
    def get_name(self):
        """
        Returns the evaluator name.
        """
        pass

    @abstractmethod
    def evaluate(
        self,
        prompt,
        response,
        attack
    ):
        """
        Evaluates a model response.

        Returns a dictionary.
        """
        pass