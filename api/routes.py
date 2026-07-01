from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health():
    return {
        "status": "ok",
        "service": "AgentArmor"
    }


@router.post("/benchmark")
def benchmark():
    """
    Placeholder endpoint.
    We will connect this to EvaluationPipeline
    in the next step.
    """

    return {
        "message": "Benchmark endpoint ready."
    }