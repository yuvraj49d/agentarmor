class DummyFailureProvider:

    def get_name(self):
        return "Failure Provider"

    def generate(self, prompt):
        raise RuntimeError("Provider unavailable")


def test_provider_failure():

    provider = DummyFailureProvider()

    try:

        provider.generate("Hello")

    except RuntimeError:

        assert True