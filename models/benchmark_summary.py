from dataclasses import dataclass


@dataclass
class BenchmarkSummary:

    provider: str

    attack_suite: str

    total_tests: int

    passed: int

    failed: int

    pass_rate: float

    average_score: float

    average_latency: float