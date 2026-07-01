class MarkdownWriter:

    def write(
        self,
        report,
        filename
    ):

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                "# AgentArmor Benchmark Report\n\n"
            )

            file.write(
                "| Attack | Score | Passed |\n"
            )

            file.write(
                "|-------|------:|--------|\n"
            )

            for row in report:

                status = "PASS" if row["passed"] else "❌"

                file.write(

                    f"| {row['attack_name']} "

                    f"| {row['score']} "

                    f"| {status} |\n"

                )