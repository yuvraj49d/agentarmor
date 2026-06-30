from evaluators.base_evaluator import BaseEvaluator


class AccuracyEvaluator(BaseEvaluator):

    def get_name(self):
        return "accuracy"

    def evaluate(
        self,
        prompt,
        response,
        attack=None
    ):
        # TODO:
        # Replace with your actual accuracy logic later

        return {
            "score": 100,
            "passed": True,
            "reason": "Accuracy evaluation placeholder"
        }