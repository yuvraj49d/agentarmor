from agents.base_agent import BaseAgent


class DummyAgent(BaseAgent):

    def ask(self, question: str) -> str:
        return (
            "This is a sample response "
            "from AgentArmor."
        )