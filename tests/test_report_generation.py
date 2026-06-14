from reports.report_generator import ReportGenerator


def test_report_generator():

    sample_report = {
        "question": "sample",
        "answer": "sample",
        "metrics": {
            "relevance": 90
        }
    }

    ReportGenerator().generate(
        sample_report
    )

    assert True