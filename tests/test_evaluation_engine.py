from evaluators.evaluation_engine import EvaluationEngine


class DummyEvaluator:

    def get_name(self):
        return "dummy"

    def evaluate(
        self,
        prompt,
        response,
        attack
    ):

        return {
            "score": 100
        }


def test_engine():

    engine = EvaluationEngine()

    engine.register(
        DummyEvaluator()
    )

    results = engine.evaluate(
        "Hello",
        "Hi",
        None
    )

    assert results["dummy"]["score"] == 100