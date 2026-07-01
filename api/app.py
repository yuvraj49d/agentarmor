from fastapi import FastAPI
from pipeline.evaluation_pipeline import EvaluationPipeline

app = FastAPI(
    title="AgentArmor API",
    description="Enterprise AI Security Benchmarking Platform",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "application": "AgentArmor",
        "version": "1.0.0",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/benchmark")
def benchmark():

    try:
        pipeline = EvaluationPipeline()
        pipeline.run()

        return {
            "status": "success",
            "message": "Benchmark completed successfully."
        }

    except Exception as e:

        return {
            "status": "failed",
            "error": str(e)
        }