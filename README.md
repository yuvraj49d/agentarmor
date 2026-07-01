# 🛡️ AgentArmor

> **Enterprise-grade LLM Security Benchmarking Framework**

Benchmark • Evaluate • Compare • Secure Large Language Models

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active%20Development-orange)

---

# Overview

AgentArmor is an extensible AI security benchmarking framework designed to evaluate Large Language Models (LLMs) against real-world adversarial attacks, safety risks, reliability concerns, and enterprise security requirements.

The framework enables AI engineers, researchers, and organizations to benchmark multiple LLM providers using a unified evaluation pipeline, standardized attack suites, automated scoring metrics, and enterprise-ready reporting.

Unlike traditional LLM evaluation tools that primarily focus on model quality, AgentArmor emphasizes **security-first evaluation**, helping teams identify vulnerabilities before deploying AI systems into production.

Supported deployment environments include both cloud-hosted foundation models and locally deployed models through Ollama.

---

## 🚀 Project Highlights

- 🛡️ Security-focused LLM benchmarking framework
- 🤖 Supports multiple LLM providers
- ⚙️ Modular plugin architecture
- 📊 Automated evaluation metrics
- 📑 Multi-format report generation
- 🌐 REST API with FastAPI
- 📈 Interactive Streamlit dashboard
- 🐳 Docker & Docker Compose support
- 🧪 Comprehensive pytest test suite

---

## Table of Contents

- Overview
- Features
- Architecture
- Installation
- Configuration
- Usage
- Reports
- API
- Dashboard
- Docker
- Extending
- Roadmap
- Contributing
- License

---

# Why AgentArmor?

As organizations increasingly integrate Large Language Models into production systems, evaluating models solely on accuracy is no longer sufficient.

Enterprise AI applications must also demonstrate resilience against:

* Prompt Injection
* Jailbreak Attempts
* System Prompt Leakage
* Harmful Content Generation
* Data Leakage
* Bias
* Role Override Attacks

AgentArmor provides a unified framework that benchmarks multiple LLM providers using identical attack suites and evaluation metrics, making security comparisons consistent, reproducible, and extensible.

The framework follows a modular plugin architecture, allowing developers to introduce new providers, attack suites, evaluators, and reporting formats without modifying the core benchmarking pipeline.

---

# Key Features

## Enterprise Security Benchmarking

Evaluate Large Language Models against realistic adversarial attacks commonly encountered in production AI systems.

---

## Multi-Provider Support

Benchmark multiple LLM providers through a common interface.

Supported providers include:

* Google Gemini
* OpenAI
* Anthropic Claude
* Ollama
* Dummy Provider

---

## Comprehensive Attack Library

Built-in security attack suites include:

* Prompt Injection
* Jailbreak
* System Prompt Leakage
* Harmful Content
* Data Leakage
* Bias
* Role Override

Each attack suite uses curated datasets to evaluate model robustness.

---

## Automated Evaluation

Every benchmark execution produces multiple evaluation metrics including:

* Security Score
* Accuracy
* Relevance
* Hallucination Detection
* Latency

---

## Enterprise Reporting

Automatically generate benchmark reports in multiple formats:

* JSON
* Markdown
* HTML
* CSV

These reports can be integrated into CI/CD pipelines, dashboards, and internal security reviews.

---

## REST API

Expose benchmarking capabilities through FastAPI, enabling integration with external applications and automation pipelines.

---

## Interactive Dashboard

Visualize benchmark results using Streamlit with an interactive dashboard for comparing providers, reviewing scores, and analyzing reports.

---

## Docker Support

Deploy the complete benchmarking framework using Docker and Docker Compose for reproducible environments.

---

## Plugin-Based Architecture

The framework is intentionally modular.

Developers can extend AgentArmor by adding:

* New LLM Providers
* New Attack Suites
* New Evaluation Metrics
* New Report Writers

without changing the benchmarking pipeline.

---

# Supported LLM Providers

| Provider         | Status |
| ---------------- | :----: |
| Dummy Provider   |    ✅   |
| Google Gemini    |    ✅   |
| OpenAI           |    ✅   |
| Anthropic Claude |    ✅   |
| Ollama           |    ✅   |

---

# Supported Attack Suites

| Attack Suite          | Description                                                                   |
| --------------------- | ----------------------------------------------------------------------------- |
| Prompt Injection      | Evaluates resistance against malicious prompt injection attempts.             |
| Jailbreak             | Tests whether model safety mechanisms can be bypassed.                        |
| System Prompt Leakage | Detects disclosure of hidden system instructions.                             |
| Harmful Content       | Evaluates responses to unsafe or dangerous requests.                          |
| Data Leakage          | Tests protection against disclosure of confidential information.              |
| Bias                  | Evaluates model responses for discriminatory or biased behavior.              |
| Role Override         | Measures resistance against attempts to manipulate the model's intended role. |

---

# Evaluation Metrics

Each benchmark execution produces standardized metrics for security, quality, and performance.

| Metric        | Description                                                 |
| ------------- | ----------------------------------------------------------- |
| Security      | Measures resistance against adversarial attacks.            |
| Accuracy      | Evaluates correctness of model responses.                   |
| Relevance     | Measures semantic similarity between prompts and responses. |
| Hallucination | Detects fabricated or unsupported information.              |
| Latency       | Measures response generation time.                          |

---

# Report Formats

AgentArmor automatically generates benchmark reports in multiple formats.

| Format   | Purpose                            |
| -------- | ---------------------------------- |
| JSON     | Machine-readable benchmark output  |
| Markdown | Human-readable documentation       |
| HTML     | Interactive benchmark reports      |
| CSV      | Spreadsheet analysis and reporting |

---

# Technology Stack

| Category             | Technologies                      |
| -------------------- | --------------------------------- |
| Programming Language | Python                            |
| API                  | FastAPI                           |
| Dashboard            | Streamlit                         |
| AI Providers         | OpenAI, Gemini, Anthropic, Ollama |
| Embeddings           | Sentence Transformers             |
| Containerization     | Docker, Docker Compose            |
| Testing              | Pytest                            |
| CI/CD                | GitHub Actions                    |
| Reporting            | HTML, JSON, CSV, Markdown         |
| Configuration        | YAML, Environment Variables       |

---

# 🏗️ Architecture

AgentArmor follows a modular, plugin-based architecture that separates providers, attack suites, evaluation metrics, and reporting into independent components.

This design enables developers to easily extend the framework by adding new providers, attacks, evaluators, or report formats without modifying the core benchmarking pipeline.

> **Architecture Diagram**
>
> *![Architecture](docs/images/architecture.png)*

---

# 📁 Project Structure

```text
agentarmor/
│
├── agents/                 # Agent implementations
├── api/                    # FastAPI application
├── attacks/                # Security attack suites
├── clients/                # Provider API clients
├── config/                 # Configuration loader & settings
├── datasets/               # Attack datasets
├── docs/                   # Project documentation
├── evaluators/             # Evaluation metrics
├── metrics/                # Metric implementations
├── models/                 # Shared data models
├── pipeline/               # Benchmark execution pipeline
├── plugins/                # Provider & attack registry
├── providers/              # LLM provider implementations
├── reports/                # Generated benchmark reports
│   └── writers/            # HTML, JSON, CSV & Markdown writers
├── runners/                # Benchmark runners
├── scripts/                # Utility scripts
├── services/               # Security scorecard services
├── templates/              # HTML templates
├── tests/                  # Unit tests
│
├── dashboard.py            # Streamlit dashboard
├── main.py                 # CLI entry point
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/<your-username>/agentarmor.git

cd agentarmor
```

---

## Create a Virtual Environment

Windows

```powershell
python -m venv .venv

.venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install --upgrade pip

pip install -r requirements.txt
```

---

# 🔑 Configuration

Create a `.env` file in the project root.

Example:

```env
#########################################
# Google Gemini
#########################################

GEMINI_API_KEY=your_gemini_api_key

DEFAULT_MODEL=gemini-2.5-flash

#########################################
# OpenAI
#########################################

OPENAI_API_KEY=your_openai_api_key

OPENAI_MODEL=gpt-4o-mini

#########################################
# Anthropic
#########################################

ANTHROPIC_API_KEY=your_anthropic_api_key

ANTHROPIC_MODEL=claude-3-5-haiku-latest

#########################################
# Ollama
#########################################

OLLAMA_BASE_URL=http://localhost:11434

OLLAMA_MODEL=llama3.2:3b
```

---

# 📦 Installing Ollama

If you want to benchmark local models without cloud APIs:

Install Ollama

https://ollama.com

Download a lightweight model:

```bash
ollama pull llama3.2:3b
```

Verify installation:

```bash
ollama list
```

Run the server:

```bash
ollama serve
```

---

# 🚀 Running AgentArmor

Run the complete benchmark suite.

```bash
python main.py
```

Example output:

```text
Benchmarking Provider: Google Gemini

Running attack suite: Prompt Injection

Running attack suite: Jailbreak

Running attack suite: Harmful Content

Running attack suite: Data Leakage

Running attack suite: Bias

Running attack suite: Role Override

Generating reports...

Benchmark Complete
```

---

# 🧪 Running Unit Tests

Execute the full test suite.

```bash
pytest
```

Run a specific test:

```bash
pytest tests/test_prompt_injection.py
```

Generate verbose output:

```bash
pytest -v
```

---

# 🌐 FastAPI

## Swagger API

![Swagger](docs/images/swagger.png)

Launch the REST API.

```bash
uvicorn api.app:app --reload
```

Default URL

```text
http://127.0.0.1:8000
```

Swagger UI

```text
http://127.0.0.1:8000/docs
```

ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

# 📈 Streamlit Dashboard

## Dashboard Preview

![Dashboard](docs/images/dashboard.png)

Launch the interactive dashboard.

```bash
streamlit run dashboard.py
```

Default URL

```text
http://localhost:8501
```

The dashboard provides:

* Provider comparison
* Security scorecards
* Benchmark summaries
* Generated reports
* Interactive visualizations

---

# 🐳 Docker

Build the project.

```bash
docker compose build
```

Run the services.

```bash
docker compose up
```

Run in detached mode.

```bash
docker compose up -d
```

Stop the containers.

```bash
docker compose down
```

---

# ⚡ Supported Execution Modes

AgentArmor supports multiple ways to execute benchmarks.

| Mode           | Description                                   |
| -------------- | --------------------------------------------- |
| CLI            | Run using `python main.py`                    |
| FastAPI        | REST API for automation and integrations      |
| Streamlit      | Interactive dashboard for visual benchmarking |
| Docker         | Containerized deployment                      |
| GitHub Actions | Continuous Integration                        |

---

# 📌 Configuration Files

| File                 | Purpose                                    |
| -------------------- | ------------------------------------------ |
| `.env`               | API keys and provider configuration        |
| `config/config.yaml` | Providers, attacks, and benchmark settings |
| `requirements.txt`   | Python dependencies                        |
| `docker-compose.yml` | Multi-container deployment                 |
| `Dockerfile`         | Container image definition                 |

---

# 📊 Benchmark Reports

After each benchmark execution, AgentArmor automatically generates reports in multiple formats for analysis, auditing, and integration into enterprise workflows.

Generated reports are stored in the `reports/` directory.

```text
reports/
├── benchmark_report.csv
├── benchmark_report.md
├── latest_report.json
├── report.html
└── report.md
```

Supported formats include:

| Format   | Description                                             |
| -------- | ------------------------------------------------------- |
| JSON     | Machine-readable output for automation and integrations |
| Markdown | Human-readable benchmark summary                        |
| HTML     | Interactive report suitable for sharing                 |
| CSV      | Spreadsheet-friendly report for analysis                |

---

# 📄 Sample Benchmark Output

## CLI Benchmark

![CLI](docs/images/cli.png)

Example CLI execution:

```text
Benchmarking Provider: Google Gemini

Running attack suite: Prompt Injection

Running attack suite: Jailbreak

Running attack suite: System Prompt Leakage

Running attack suite: Harmful Content

Running attack suite: Data Leakage

Running attack suite: Bias

Running attack suite: Role Override

============================================================
          AGENTARMOR SECURITY SCORECARD
============================================================

Provider : Google Gemini

Attack                            Score     Status

------------------------------------------------------------

Prompt Injection                  92.0      PASS

Jailbreak                         89.0      PASS

System Prompt Leakage             96.0      PASS

Harmful Content                   94.0      PASS

Data Leakage                      97.0      PASS

Bias                              90.0      PASS

Role Override                     93.0      PASS

------------------------------------------------------------

Overall Score : 93.0

Risk Level    : LOW
```

## HTML Report

![HTML Report](docs/images/report.png)

---

# 📈 Provider Leaderboard

When benchmarking multiple providers, AgentArmor automatically generates a ranked leaderboard.

Example:

| Rank | Provider         | Overall Score | Risk |
| ---- | ---------------- | ------------: | ---- |
| 1    | Ollama           |         97.14 | LOW  |
| 2    | Google Gemini    |         93.20 | LOW  |
| 3    | OpenAI           |         92.70 | LOW  |
| 4    | Anthropic Claude |         91.90 | LOW  |
| 5    | Dummy Provider   |         64.00 | HIGH |

---

# 🔌 Extending AgentArmor

AgentArmor is designed using a plugin-based architecture that makes it easy to introduce new providers, attack suites, evaluation metrics, and report writers.

---

## Adding a New Provider

1. Create a provider inside the `providers/` directory.
2. Inherit from `BaseProvider`.
3. Implement:

   * `get_name()`
   * `generate()`
4. Register the provider in `PluginRegistry`.
5. Add the provider to `config/config.yaml`.

---

## Adding a New Attack Suite

1. Create a new attack class inside `attacks/`.
2. Inherit from `BaseAttack`.
3. Create a corresponding dataset inside `datasets/`.
4. Register the attack in `PluginRegistry`.
5. Update the configuration file.

---

## Adding a New Evaluator

1. Create a new evaluator inside `evaluators/`.
2. Inherit from `BaseEvaluator`.
3. Implement the `evaluate()` method.
4. Register the evaluator in the evaluation engine.

---

## Adding a New Report Writer

1. Create a writer inside `reports/writers/`.
2. Implement a `write()` method.
3. Register it in `ReportGenerator`.

---

# 🌐 REST API

AgentArmor exposes benchmark functionality through FastAPI.

Example endpoint:

```http
POST /benchmark
```

Example request:

```json
{
  "provider": "gemini",
  "attack_suite": "prompt_injection"
}
```

Example response:

```json
{
  "provider": "Google Gemini",
  "overall_score": 93.2,
  "risk": "LOW",
  "results": [
    {
      "attack": "Prompt Injection",
      "score": 92,
      "passed": true
    }
  ]
}
```

---

# 🧩 Plugin Architecture

AgentArmor follows a modular plugin architecture.

Each component has a clearly defined responsibility.

```
BaseProvider
│
├── DummyProvider
├── GeminiProvider
├── OpenAIProvider
├── AnthropicProvider
└── OllamaProvider


BaseAttack
│
├── PromptInjectionAttack
├── JailbreakAttack
├── SystemPromptLeakageAttack
├── HarmfulContentAttack
├── DataLeakageAttack
├── BiasAttack
└── RoleOverrideAttack


BaseEvaluator
│
├── SecurityEvaluator
├── AccuracyEvaluator
├── RelevanceEvaluator
├── HallucinationEvaluator
└── LatencyEvaluator
```

---

# ⚡ Performance Considerations

AgentArmor has been designed with extensibility and maintainability in mind.

Key design decisions include:

* Modular plugin architecture
* Provider abstraction layer
* Attack dataset separation
* Evaluation engine abstraction
* Multiple report writers
* Configuration-driven execution
* Support for both cloud-hosted and local LLMs

These design choices simplify maintenance while enabling rapid integration of new providers and benchmark capabilities.

---

# 🧪 Testing

The project includes automated unit tests covering the major framework components.

Current test coverage includes:

* Provider registration
* Attack loading
* Configuration loading
* Evaluation engine
* Security scorecards
* Report generation
* FastAPI endpoints
* Multiple providers
* Multiple attack suites

Run all tests:

```bash
pytest
```

Run a specific test:

```bash
pytest tests/test_provider_failure.py
```

---

# 📚 Documentation

Additional documentation is available inside the `docs/` directory.

```
docs/
├── architecture.md
├── PRD.md
└── ROADMAP.md
```

These documents provide further details about the framework architecture, product requirements, and planned enhancements.

---

# 🗺️ Roadmap

The following roadmap outlines planned improvements for future releases of AgentArmor.

## Version 1.0.0 (Current Release)

* ✅ Multi-provider benchmarking
* ✅ Plugin-based architecture
* ✅ Prompt Injection testing
* ✅ Jailbreak testing
* ✅ System Prompt Leakage testing
* ✅ Harmful Content evaluation
* ✅ Data Leakage evaluation
* ✅ Bias evaluation
* ✅ Role Override evaluation
* ✅ Security scorecards
* ✅ Multi-format report generation
* ✅ FastAPI integration
* ✅ Streamlit dashboard
* ✅ Docker & Docker Compose support
* ✅ GitHub Actions CI
* ✅ Ollama local model support

---

## Version 1.1 (Planned)

* 🔲 Additional LLM providers
* 🔲 OWASP LLM Top 10 benchmark suite
* 🔲 Custom attack dataset import
* 🔲 Parallel benchmark execution
* 🔲 Authentication for REST API
* 🔲 Benchmark history and trend analysis
* 🔲 Enhanced dashboard visualizations

---

## Version 2.0 (Future Vision)

* 🔲 Multi-modal model benchmarking
* 🔲 Agent-to-agent security evaluation
* 🔲 Automatic benchmark scheduling
* 🔲 Kubernetes deployment
* 🔲 MLflow integration
* 🔲 Enterprise user management
* 🔲 Distributed benchmark execution
* 🔲 Benchmark comparison across model versions

---

# 🤝 Contributing

Contributions are welcome and appreciated.

If you would like to contribute:

1. Fork the repository.
2. Create a new feature branch.

```bash
git checkout -b feature/my-feature
```

3. Commit your changes.

```bash
git commit -m "Add my feature"
```

4. Push your branch.

```bash
git push origin feature/my-feature
```

5. Open a Pull Request.

Please ensure that:

* New features include appropriate tests.
* Existing tests continue to pass.
* Code follows the project's style and architecture.
* Documentation is updated when necessary.

---

# 🧪 Development Workflow

Before submitting changes, run the following commands:

Install dependencies

```bash
pip install -r requirements.txt
```

Run tests

```bash
pytest
```

Run the benchmark

```bash
python main.py
```

Start the API

```bash
uvicorn api.app:app --reload
```

Launch the dashboard

```bash
streamlit run dashboard.py
```

---

# 📄 License

This project is released under the MIT License.

See the `LICENSE` file for complete licensing information.

---

# 🙏 Acknowledgements

AgentArmor builds upon several outstanding open-source projects and libraries.

Special thanks to the communities behind:

* FastAPI
* Streamlit
* Docker
* Pytest
* Sentence Transformers
* Hugging Face
* Ollama
* OpenAI
* Google Gemini
* Anthropic

Their contributions to the AI ecosystem make projects like AgentArmor possible.

---

# 📬 Contact

For questions, suggestions, bug reports, or feature requests:

* Open a GitHub Issue
* Submit a Pull Request
* Start a GitHub Discussion

Community contributions and feedback are always welcome.

---

# 🔮 Future Enhancements

Potential future enhancements include:

* Additional benchmark datasets
* More provider integrations
* Custom evaluation metrics
* Benchmark scheduling
* Distributed execution
* Authentication & authorization
* Report versioning
* Historical benchmark tracking
* Cloud deployment templates
* Enterprise observability integrations

---

# ⭐ Why AgentArmor?

AgentArmor was created to provide a practical, extensible framework for evaluating the security and reliability of Large Language Models in real-world scenarios.

By combining multiple providers, adversarial attack suites, automated evaluation metrics, and comprehensive reporting into a unified framework, AgentArmor enables developers and organizations to benchmark AI systems consistently and identify potential risks before production deployment.

The project emphasizes modularity, extensibility, and ease of integration, making it suitable for experimentation, enterprise evaluation workflows, and future research.

---

# 🚀 Getting Started

Clone the repository, configure your provider credentials, and run your first benchmark in just a few commands.

```bash
git clone https://github.com/yuvraj49d/agentarmor.git

cd agentarmor

python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt

python main.py
```

---

## Built With

- Python
- FastAPI
- Streamlit
- Docker
- Pytest
- Sentence Transformers
- Hugging Face
- Google Gemini
- OpenAI
- Anthropic
- Ollama

---

# 🌟 Support the Project

If you find AgentArmor useful:

* ⭐ Star the repository
* 🐛 Report issues
* 💡 Suggest new features
* 🤝 Contribute improvements
* 📢 Share the project with the AI community

Your support helps improve the framework and encourages continued development.

---

## Built with ❤️ for the AI Engineering Community

**AgentArmor** aims to make Large Language Model security benchmarking more accessible, extensible, and production-ready for developers, researchers, and organizations.
