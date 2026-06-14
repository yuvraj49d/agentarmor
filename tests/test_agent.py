from agents.simple_agent import SimpleAgent


def test_agent_returns_response():

    agent = SimpleAgent()

    answer = agent.ask(
        "What is machine learning?"
    )

    assert answer is not None

    assert len(answer) > 0