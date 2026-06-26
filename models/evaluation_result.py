from dataclasses import dataclass
from datetime import datetime

@dataclass
class EvaluationResult:

    provider: str

    attack_name: str

    attack_category: str

    prompt: str

    response: str

    passed: bool

    score: float

    latency: float

    timestamp: datetime

    reason: str