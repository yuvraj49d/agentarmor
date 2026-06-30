from config.config_loader import ConfigLoader
from plugins.plugin_registry import PluginRegistry
from runners.benchmark_runner import BenchmarkRunner
from reports.report_generator import ReportGenerator
from dataclasses import asdict
from services.security_scorecard_service import SecurityScorecardService

class EvaluationPipeline:

    def __init__(self):

        self.config = ConfigLoader(
            "config/config.yaml"
        ).load()

        self.registry = PluginRegistry()

    def run(self):

        evaluator = self.registry.get_evaluator(
            "security"
        )

        leaderboard = []

        for provider_name in self.config["providers"]:

            provider = self.registry.get_provider(
                provider_name
            )

            print(f"\nBenchmarking Provider: {provider.get_name()}")

            try:

                all_results = []

                for attack_name in self.config["attack_suite"]:

                    attack = self.registry.get_attack(
                        attack_name
                    )

                    print(
                        f"Running attack suite: "
                        f"{attack.get_attack_name()}"
                    )

                    runner = BenchmarkRunner(
                        provider,
                        attack,
                        evaluator
                    )

                    results = runner.run()

                    all_results.extend(results)

                report = [
                    asdict(r)
                    for r in all_results
                ]

                ReportGenerator().generate(report)

                scorecard = SecurityScorecardService().generate(
                    all_results
                )

                self.print_scorecard(
                    provider.get_name(),
                    scorecard
                )

                self.print_summary(
                    provider.get_name(),
                    "All Attack Suites",
                    all_results
                )

                leaderboard.append(
                    {
                        "provider": provider.get_name(),
                        "status": "SUCCESS",
                        "score": scorecard["overall_score"],
                        "risk": scorecard["risk"],
                        "reason": ""
                    }
                )

            except Exception as e:

                print()

                print("=" * 60)
                print("Provider Failed")
                print("=" * 60)

                print(provider.get_name())
                print()
                print(str(e))

                leaderboard.append(
                    {
                        "provider": provider.get_name(),
                        "status": "FAILED",
                        "score": None,
                        "risk": None,
                        "reason": str(e)
                    }
                )

        self.print_leaderboard(
            leaderboard
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

    def print_scorecard(
        self,
        provider,
        scorecard
    ):

        print()

        print("=" * 60)
        print("          AGENTARMOR SECURITY SCORECARD")
        print("=" * 60)

        print(f"Provider : {provider}")

        print()

        print(f"{'Attack':30} {'Score':>8} {'Status':>10}")

        print("-" * 60)

        for item in scorecard["categories"]:

            status = "PASS" if item["passed"] else "FAIL"

            print(
                f"{item['attack']:30}"
                f"{item['score']:>8}"
                f"{status:>10}"
            )

        print("-" * 60)

        print(
            f"Overall Score : "
            f"{scorecard['overall_score']}"
        )

        print(
            f"Risk Level    : "
            f"{scorecard['risk']}"
        )

        print("=" * 60)

    def print_leaderboard(
        self,
        leaderboard
    ):

        successful = [
            p
            for p in leaderboard
            if p["score"] is not None
        ]

        failed = [
            p
            for p in leaderboard
            if p["score"] is None
        ]

        successful.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        print()

        print("=" * 70)
        print("AGENTARMOR PROVIDER LEADERBOARD")
        print("=" * 70)

        print(
            f"{'Rank':<6}"
            f"{'Provider':<25}"
            f"{'Status':<12}"
            f"{'Score':<10}"
            f"{'Risk'}"
        )

        print("-" * 70)

        rank = 1

        for item in successful:

            print(
                f"{rank:<6}"
                f"{item['provider']:<25}"
                f"{item['status']:<12}"
                f"{item['score']:<10}"
                f"{item['risk']}"
            )

            rank += 1

        for item in failed:

            print(
                f"{'-':<6}"
                f"{item['provider']:<25}"
                f"{item['status']:<12}"
                f"{'N/A':<10}"
                f"{'-'}"
            )

        print("=" * 70)

        if failed:

            print()

            print("Failure Details")

            print("-" * 70)

            for item in failed:

                print()

                print(item["provider"])

                print(item["reason"])