from evaluators.relevance import RelevanceEvaluator


def test_relevance():

    evaluator = RelevanceEvaluator()

    result = evaluator.evaluate(

        "What is AI?",

        "Artificial Intelligence is the simulation of human intelligence."

    )

    assert result["score"] > 50

    assert "score" in result