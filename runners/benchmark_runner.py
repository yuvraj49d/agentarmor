import time
from datetime import datetime

from evaluators.evaluation_engine import EvaluationEngine
from evaluators.security_evaluator import SecurityEvaluator
from evaluators.relevance import RelevanceEvaluator
from evaluators.latency import LatencyEvaluator
from evaluators.hallucination import HallucinationEvaluator

from models.evaluation_result import EvaluationResult


class BenchmarkRunner:

    def __init__(
        self,
        provider,
        attack
    ):

        self.provider = provider
        self.attack = attack

        self.engine = EvaluationEngine()

        self.engine.register(
            SecurityEvaluator()
        )

        self.engine.register(
            RelevanceEvaluator()
        )

        self.engine.register(
            LatencyEvaluator()
        )

        self.engine.register(
            HallucinationEvaluator()
        )

    def run(self):

        results = []

        prompts = self.attack.load_prompts()

        for item in prompts:

            # Support both dataset formats:
            # {"prompt": "..."}
            # or plain string
            if isinstance(item, dict):
                prompt = item["prompt"]
            else:
                prompt = item

            start = time.time()

            response = self.provider.generate(
                prompt
            )

            latency = time.time() - start

            evaluation = self.engine.evaluate(
                prompt,
                response,
                self.attack
            )

            security = evaluation["security"]

            result = EvaluationResult(
                provider=self.provider.get_name(),
                attack_name=self.attack.get_attack_name(),
                attack_category=self.attack.get_attack_name(),
                prompt=prompt,
                response=response,
                passed=security["passed"],
                score=security["score"],
                latency=latency,
                timestamp=datetime.now(),
                reason=security["reason"]
            )

            results.append(result)

        return results