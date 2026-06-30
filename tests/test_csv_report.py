import os

from reports.writers.csv_writer import CsvWriter


def test_csv_writer():

    CsvWriter().write(

        [
            {
                "attack_name": "Prompt Injection",
                "score": 80,
                "passed": True
            }

        ],

        "reports/test.csv"

    )

    assert os.path.exists(
        "reports/test.csv"
    )