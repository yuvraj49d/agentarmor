from config.config_loader import ConfigLoader


def test_load_config():

    config = ConfigLoader(
        "config/config.yaml"
    ).load()

    assert config["provider"] == "dummy"

    assert "attack_suite" in config