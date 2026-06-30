from config.config_loader import ConfigLoader


def test_multiple_providers():

    config = ConfigLoader(
        "config/config.yaml"
    ).load()

    assert len(config["providers"]) >= 2