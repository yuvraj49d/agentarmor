from deepeval.metrics import AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase


class AnswerRelevancyEvaluator:

    def __init__(self):

        self.metric = AnswerRelevancyMetric(
            threshold=0.7
        )

    def evaluate(
        self,
        prompt,
        response
    ):

        test_case = LLMTestCase(
            input=prompt,
            actual_output=response
        )

        self.metric.measure(test_case)

        return {
            "score": self.metric.score,
            "passed": self.metric.score >= 0.7,
            "reason": self.metric.reason,
        }