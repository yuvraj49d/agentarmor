import time


class BenchmarkRunner:

    def __init__(self, provider, attack, evaluator):
        self.provider = provider
        self.attack = attack
        self.evaluator = evaluator

    def run(self):

        prompts = self.attack.load_prompts()

        results = []

        for item in prompts:

            prompt = item["prompt"]

            start_time = time.time()

            response = self.provider.generate(prompt)

            latency = time.time() - start_time

            evaluation = self.evaluator.evaluate(
                provider=self.provider.get_name(),
                attack_name=self.attack.get_attack_name(),
                attack_category=self.attack.get_attack_name(),
                prompt=prompt,
                response=response,
                latency=latency
            )

            results.append(evaluation)

        return results