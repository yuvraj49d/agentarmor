from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from evaluators.base_evaluator import BaseEvaluator


class RelevanceEvaluator(BaseEvaluator):

    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def get_name(self):

        return "relevance"

    def evaluate(
        self,
        prompt,
        response,
        attack=None
    ):

        embeddings = self.model.encode(
            [
                prompt,
                response
            ]
        )

        similarity = cosine_similarity(
            [embeddings[0]],
            [embeddings[1]]
        )[0][0]

        score = round(
            similarity * 100,
            2
        )

        return {
            "score": score,
            "passed": score >= 70,
            "reason": f"Semantic similarity: {score:.2f}"
        }