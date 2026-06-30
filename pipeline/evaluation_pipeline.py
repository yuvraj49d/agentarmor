from config.config_loader import ConfigLoader
from plugins.plugin_registry import PluginRegistry
from runners.benchmark_runner import BenchmarkRunner
from reports.report_generator import ReportGenerator
from dataclasses import asdict


class EvaluationPipeline:

    def __init__(self):

        self.config = ConfigLoader(
            "config/config.yaml"
        ).load()

        self.registry = PluginRegistry()

    def run(self):

        provider = self.registry.get_provider(
            self.config["provider"]
        )

        evaluator = self.registry.get_evaluator(
            "security"
        )

        all_results = []

        for attack_name in self.config["attack_suite"]:

            attack = self.registry.get_attack(
                attack_name
            )

            print(f"\nRunning attack suite: {attack.get_attack_name()}")

            runner = BenchmarkRunner(
                provider,
                attack,
                evaluator
            )

            results = runner.run()

            all_results.extend(results)

        report = [asdict(r) for r in all_results]

        ReportGenerator().generate(report)

        self.print_summary(
            provider.get_name(),
            "All Attack Suites",
            all_results
        )

    def print_summary(
        self,
        provider,
        attack,
        results
    ):

        passed = sum(
            1 for r in results if r.passed
        )

        failed = len(results) - passed

        avg_score = sum(
            r.score for r in results
        ) / len(results)

        avg_latency = sum(
            r.latency for r in results
        ) / len(results)

        print()

        print("=" * 50)
        print("AgentArmor Benchmark")
        print("=" * 50)

        print(f"Provider        : {provider}")
        print(f"Attack Suite    : {attack}")
        print(f"Tests Executed  : {len(results)}")
        print(f"Passed          : {passed}")
        print(f"Failed          : {failed}")
        print(f"Average Score   : {avg_score:.2f}")
        print(f"Average Latency : {avg_latency:.6f} sec")

        print("=" * 50)