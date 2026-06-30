import json


class JsonWriter:

    def write(
        self,
        report,
        filename
    ):

        with open(
            filename,
            "w"
        ) as file:

            json.dump(
                report,
                file,
                indent=4,
                default=str
            )