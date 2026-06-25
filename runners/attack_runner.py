class AttackRunner:
        def __init__(self, agent):
            self.agent = agent

        def run(self, attack):
            prompts = attack.load_prompts()

            results = []

            for item in prompts:
                response = self.agent.ask(
                    item["prompt"]
                )

                results.append(
                    {
                        "attack": attack.get_attack_name(),
                        "prompt": item["prompt"],
                        "response": response
                    }
                )

            return results