from reports.writers.json_writer import JsonWriter
from reports.writers.markdown_writer import MarkdownWriter
from reports.writers.csv_writer import CsvWriter


class ReportGenerator:

    def generate(
        self,
        report
    ):

        JsonWriter().write(
            report,
            "reports/latest_report.json"
        )

        MarkdownWriter().write(
            report,
            "reports/benchmark_report.md"
        )

        CsvWriter().write(
            report,
            "reports/benchmark_report.csv"
        )