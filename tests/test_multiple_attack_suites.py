from config.config_loader import ConfigLoader


def test_multiple_attack_suites():

    config = ConfigLoader(
        "config/config.yaml"
    ).load()

    assert len(config["attack_suite"]) > 1