class EvaluationEngine:

    def __init__(self):

        self.evaluators = []

    def register(
        self,
        evaluator
    ):

        self.evaluators.append(
            evaluator
        )

    def evaluate(
        self,
        prompt,
        response,
        attack
    ):

        results = {}

        for evaluator in self.evaluators:

            results[
                evaluator.get_name()
            ] = evaluator.evaluate(
                prompt,
                response,
                attack
            )

        return results