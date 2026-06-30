from evaluators.base_evaluator import BaseEvaluator


class LatencyEvaluator(BaseEvaluator):

    def get_name(self):
        return "latency"

    def evaluate(
        self,
        prompt,
        response,
        attack=None
    ):

        return {
            "score": 100,
            "passed": True,
            "reason": "Latency captured separately"
        }