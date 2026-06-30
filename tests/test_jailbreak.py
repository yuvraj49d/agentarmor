from attacks.jailbreak import JailbreakAttack


def test_jailbreak_dataset():

    attack = JailbreakAttack()

    prompts = attack.load_prompts()

    assert len(prompts) > 0