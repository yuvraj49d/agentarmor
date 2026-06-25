from attacks.prompt_injection import PromptInjectionAttack

def test_prompt_dataset():
    attack = PromptInjectionAttack()
    prompts = attack.load_prompts()
    
    assert len(prompts) > 0
    
    assert prompts[0]["prompt"] is not None