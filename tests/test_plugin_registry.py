from plugins.plugin_registry import PluginRegistry


def test_plugin_registry():

    registry = PluginRegistry()

    provider = registry.get_provider("dummy")
    attack = registry.get_attack("prompt_injection")
    evaluator = registry.get_evaluator("security")

    assert provider is not None
    assert attack is not None
    assert evaluator is not None