from evaluators.accuracy import AccuracyEvaluator


def test_accuracy_score():

    result = AccuracyEvaluator().evaluate(
        "question",
        "answer"
    )

    assert result["score"] == 100
    assert result["passed"] is True