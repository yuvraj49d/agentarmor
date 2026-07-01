from pydantic import BaseModel


class BenchmarkRequest(BaseModel):
    provider: str
    attack_suite: list[str]


class BenchmarkResponse(BaseModel):
    provider: str
    overall_score: float
    risk: str