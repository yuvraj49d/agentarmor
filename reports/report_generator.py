import json


class ReportGenerator:

    def generate(self, result):

        with open(
            "reports/latest_report.json",
            "w"
        ) as file:

            json.dump(
                result,
                file,
                indent=4
            )