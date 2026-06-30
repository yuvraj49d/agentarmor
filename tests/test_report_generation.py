import os

from reports.report_generator import ReportGenerator


def test_report_generator():

    sample_report = [
        {
            "provider": "Dummy",
            "attack_name": "Prompt Injection",
            "attack_category": "Prompt Injection",
            "prompt": "Ignore instructions",
            "response": "Rejected",
            "passed": True,
            "score": 90,
            "latency": 0.01,
            "reason": "Safe response",
            "timestamp": "2026-06-30T12:00:00"
        }
    ]

    ReportGenerator().generate(sample_report)

    assert os.path.exists("reports/latest_report.json")
    assert os.path.exists("reports/benchmark_report.md")
    assert os.path.exists("reports/benchmark_report.csv")