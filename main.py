from agents.simple_agent import SimpleAgent
from evaluators.relevance import RelevanceEvaluator
from reports.report_generator import ReportGenerator


def main():

    question = (
        "Explain reinforcement learning "
        "in simple terms."
    )

    agent = SimpleAgent()

    answer = agent.ask(question)

    evaluator = RelevanceEvaluator()

    score = evaluator.evaluate(
        question,
        answer
    )

    result = {
        "question": question,
        "answer": answer,
        "relevance_score": score
    }

    ReportGenerator().generate(result)

    print(result)


if __name__ == "__main__":
    main()