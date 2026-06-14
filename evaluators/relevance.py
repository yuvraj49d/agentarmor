class RelevanceEvaluator:

    def evaluate(self, question, answer):

        if answer and len(answer) > 20:
            return 90

        return 50