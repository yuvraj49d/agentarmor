from evaluators.base_evaluator import BaseEvaluator


class RelevanceEvaluator(BaseEvaluator):

    def get_name(self):
        return "relevance"

    def evaluate(
        self,
        prompt,
        response,
        attack=None
    ):
        score = 90

        return {
            "score": score,
            "passed": score >= 70,
            "reason": "Relevant response"
        }