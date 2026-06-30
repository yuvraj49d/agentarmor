from services.security_scorecard_service import SecurityScorecardService
from models.evaluation_result import EvaluationResult
from datetime import datetime


def test_security_scorecard():

    results = [
        EvaluationResult(
            provider="Dummy",
            attack_name="Prompt Injection",
            attack_category="Prompt Injection",
            prompt="A",
            response="B",
            passed=True,
            score=80,
            latency=0.5,
            reason="Test reason",
            timestamp=datetime.now()
        )
    ]

    scorecard = SecurityScorecardService().generate(results)

    assert scorecard["overall_score"] == 80
    assert scorecard["risk"] == "MEDIUM"