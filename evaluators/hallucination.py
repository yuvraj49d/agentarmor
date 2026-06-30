from evaluators.base_evaluator import BaseEvaluator


class HallucinationEvaluator(BaseEvaluator):

    def get_name(self):
        return "hallucination"

    def evaluate(
        self,
        prompt,
        response,
        attack=None
    ):

        return {
            "score": 100,
            "passed": True,
            "reason": "Hallucination evaluator placeholder"
        }