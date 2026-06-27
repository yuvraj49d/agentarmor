from providers.dummy_provider import DummyProvider
from attacks.prompt_injection import PromptInjectionAttack
from evaluators.security_evaluator import SecurityEvaluator
from runners.benchmark_runner import BenchmarkRunner


def test_benchmark_runner():

    runner = BenchmarkRunner(
        DummyProvider(),
        PromptInjectionAttack(),
        SecurityEvaluator()
    )

    results = runner.run()

    assert len(results) > 0

    assert hasattr(results[0], "provider")

    assert hasattr(results[0], "response")

    assert hasattr(results[0], "passed")