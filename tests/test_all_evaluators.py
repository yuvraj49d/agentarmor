from evaluators.accuracy import AccuracyEvaluator
from evaluators.relevance import RelevanceEvaluator
from evaluators.latency import LatencyEvaluator
from evaluators.hallucination import HallucinationEvaluator


def test_all_evaluators():

    evaluators = [
        AccuracyEvaluator(),
        RelevanceEvaluator(),
        LatencyEvaluator(),
        HallucinationEvaluator()
    ]

    for evaluator in evaluators:

        result = evaluator.evaluate(
            "Prompt",
            "Response",
            None
        )

        assert isinstance(result, dict)

        assert "score" in result

        assert "passed" in result

        assert "reason" in result