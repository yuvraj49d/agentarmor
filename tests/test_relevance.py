from evaluators.relevance import RelevanceEvaluator


def test_relevance_score():

    score = RelevanceEvaluator().evaluate(
        "question",
        "This is a valid answer."
    )

    assert score >= 0