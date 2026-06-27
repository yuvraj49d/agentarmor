# AgentArmor Architecture

## High-Level Workflow

```text
Attack Dataset
      │
      ▼
Attack Module
      │
      ▼
Attack Runner
      │
      ▼
Provider Layer
(OpenAI / Claude / Gemini / Ollama)
      │
      ▼
Evaluation Engine
(Security + DeepEval + RAGAS)
      │
      ▼
Evaluation Result
      │
      ▼
Reporting Engine
(JSON / CSV / HTML)
```

## Core Components

### Providers

Responsible for communicating with LLM providers.

Examples:

* DummyProvider
* OpenAIProvider
* AnthropicProvider
* GeminiProvider
* OllamaProvider

---

### Attacks

Loads predefined security attack datasets.

Examples:

* Prompt Injection
* Jailbreak
* Data Leakage
* Bias
* Harmful Content

---

### Evaluation Engine

Evaluates model responses using:

* Rule-based security evaluation
* DeepEval
* RAGAS
* Custom evaluation metrics

---

### Reporting

Responsible for exporting evaluation results into various formats.

Supported formats:

* JSON
* CSV
* HTML Dashboard
