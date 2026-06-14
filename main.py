import time

from agents.dummy_agent import DummyAgent

from evaluators.relevance import RelevanceEvaluator
from evaluators.accuracy import AccuracyEvaluator
from evaluators.hallucination import HallucinationEvaluator
from evaluators.latency import LatencyEvaluator

from reports.report_generator import ReportGenerator

from scripts.dataset_loader import load_dataset


def main():

    dataset = load_dataset(
        "datasets/sample_dataset.json"
    )

    agent = DummyAgent()

    all_results = []

    for item in dataset:

        question = item["question"]

        start_time = time.time()

        answer = agent.ask(question)

        end_time = time.time()

        response_time = end_time - start_time

        relevance_score = (
            RelevanceEvaluator()
            .evaluate(question, answer)
        )

        accuracy_score = (
            AccuracyEvaluator()
            .evaluate(question, answer)
        )

        hallucination_score = (
            HallucinationEvaluator()
            .evaluate(question, answer)
        )

        latency_score = (
            LatencyEvaluator()
            .evaluate(response_time)
        )

        result = {
            "question": question,
            "answer": answer,
            "metrics": {
                "relevance": relevance_score,
                "accuracy": accuracy_score,
                "hallucination": hallucination_score,
                "latency": latency_score
            }
        }

        all_results.append(result)

    ReportGenerator().generate(all_results)

    print("\n===== AgentArmor Evaluation Results =====\n")

    for result in all_results:

        print(f"Question: {result['question']}")
        print(f"Answer: {result['answer']}")
        print(
            f"Metrics: {result['metrics']}"
        )
        print("-" * 50)


if __name__ == "__main__":
    main()