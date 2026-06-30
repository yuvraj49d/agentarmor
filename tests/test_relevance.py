from evaluators.relevance import RelevanceEvaluator


def test_relevance_score():

    result = RelevanceEvaluator().evaluate(
        "question",
        "This is a valid answer."
    )

    assert result["score"] == 90
    assert result["passed"] is True