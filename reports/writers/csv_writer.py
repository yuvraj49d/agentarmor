import csv


class CsvWriter:

    def write(
        self,
        report,
        filename
    ):

        if not report:
            return

        with open(
            filename,
            "w",
            newline=""
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=report[0].keys()
            )

            writer.writeheader()

            writer.writerows(report)