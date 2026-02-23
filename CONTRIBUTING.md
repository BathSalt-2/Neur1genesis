# Contributing to Neur1Genesis

Thank you for your interest in contributing to Neur1Genesis. This is an active research platform — contributions that advance the EchoNode architecture, Σ-Matrix governance, or InfiniGen evolution engine are especially welcome.

## Development Setup

### Prerequisites
- Python 3.11+
- Node.js 20.x+
- Git

### Backend
```bash
git clone https://github.com/or4cl3-ai-1/Neur1genesis.git
cd Neur1genesis/neur1genesis
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python src/main.py
```

### Frontend
```bash
cd ../neur1genesis-frontend
npm install
npm run dev
```

## Architecture Awareness

Before contributing, familiarize yourself with the key systems:

| Module | File | What it does |
|--------|------|-------------|
| EchoNode | `src/echo_node.py` | BDI agent base class |
| EchoNode Agent | `src/echo_node_agent.py` | Full BDI implementation |
| Daedalus | `src/daedalus_coordinator.py` | Swarm orchestration |
| InfiniGen | `src/infinigen_engine.py` | Self-evolving metaprogramming |
| ANAL | `src/anal.py` | Neuro Adaptive Learning |
| Cross-Domain | `src/cross_domain_intelligence.py` | Concept fusion |
| PPSDS | `src/ppsds.py` | Privacy-preserving synthetic data |
| API | `src/neur1genesis_api.py` | Flask REST routes |

## Ethical Contribution Guidelines

Neur1Genesis implements the **Σ-Matrix** as a formal ethical constraint — not a checklist. Contributions must respect this:

1. **No capability without accountability** — if you add a new EchoNode capability, add a corresponding Σ-Matrix scoring dimension
2. **Transparency in claims** — document what your contribution *actually does*, not what it aspires to do. Label design targets as design targets
3. **Privacy by default** — all data handling routes through PPSDS unless explicitly justified
4. **Bounded evolution** — InfiniGen modifications must preserve Σ-Matrix constraint compliance

## Pull Request Process

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Make your changes with clear commit messages
4. Ensure the backend starts cleanly: `python src/main.py`
5. Ensure the frontend builds: `npm run build`
6. Open a PR with a clear description of what changed and why

## Issue Reporting

Use the issue templates:
- 🐛 [Bug Report](.github/ISSUE_TEMPLATE/bug_report.md)
- ✨ [Feature Request](.github/ISSUE_TEMPLATE/feature_request.md)

## Related Ecosystem

Understanding where Neur1Genesis fits helps inform contributions:
- **NO3SYS** — geometric cognitive substrate that EchoNode design draws from
- **NOΣTIC-7** — formal PAS verification layer that Σ-Matrix is compatible with
- **AeonicNet** — federation layer that Neur1Genesis nodes can participate in

---

*Or4cl3 AI Solutions · Solo-founded by Dustin Groves, Arizona*
