from evaluators.accuracy import AccuracyEvaluator


def test_accuracy_score():

    score = AccuracyEvaluator().evaluate(
        "question",
        "answer"
    )

    assert score >= 0