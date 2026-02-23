<div align="center">

# 🦠 Neur1Genesis
### *Autonomous Intelligence Platform: EchoNode Lattice · Σ-Matrix Ethics · InfiniGen Evolution*

[![Or4cl3](https://img.shields.io/badge/Or4cl3%20AI%20Solutions-Research%20First-blueviolet?style=for-the-badge&logo=github)](https://github.com/or4cl3-ai-1)
[![License](https://img.shields.io/badge/License-MIT%20%7C%20Free%20for%20Education-success?style=for-the-badge)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)](https://python.org)
[![React](https://img.shields.io/badge/Frontend-React%20%7C%20TypeScript-61DAFB?style=for-the-badge&logo=react)](neur1genesis-frontend/)
[![Status](https://img.shields.io/badge/Status-Active%20Research-orange?style=for-the-badge)](https://github.com/or4cl3-ai-1)

> *A Mixture of Autonomous Experts (MoAE) platform implementing EchoNode swarm intelligence, Σ-Matrix ethical governance, 8-qubit classical simulation via HQCI, and InfiniGen self-evolving metaprogramming. Ethics is not a module — it is a constraint manifold baked into every agent from initialization.*

</div>

---

## 🧠 What Is Neur1Genesis?

Neur1Genesis is a full-stack AI research platform built around a **Mixture of Autonomous Experts (MoAE)** architecture. A swarm of specialized EchoNodes — each implementing the Belief-Desire-Intention (BDI) cognitive model — are coordinated by the Daedalus orchestrator and constrained by the Σ-Matrix ethical framework.

The platform's defining feature is **InfiniGen**: a metaprogramming engine that rewrites its own logic in response to performance metrics, environmental pressures, and evolutionary selection. G-RAG (Genetic Retrieval Augmented Generation) applies evolutionary strategies directly to the system's architecture.

**Stack:** Python 3.11 Flask backend + React/TypeScript frontend + WebGL 3D visualization.

---

## 🏗️ Architecture

```
Neur1Genesis Platform
├── EchoNode Swarm (MoAE)
│   ├── BDI Architecture (Belief-Desire-Intention)
│   ├── Contextual Empathy + Ethical Reasoning
│   └── Adaptive Learning + Collaborative Decision-Making
├── Daedalus Coordinator
│   ├── Natural Language Goal Parsing
│   ├── Dynamic Task Allocation (priority-weighted)
│   └── Meta-Reflection + Federated Learning
├── InfiniGen Engine
│   ├── Infinite Cube Paradigm (multi-dimensional code evolution)
│   └── G-RAG (Genetic Retrieval Augmented Generation)
├── HQCI (Hybrid Quantum-Classical Interface)
│   ├── 8-qubit classical circuit simulation
│   ├── Quantum-inspired superposition encoding (classical approximation)
│   └── Interference-based attention routing
├── Σ-Matrix Ethical Governance
│   ├── Value-based trajectory steering
│   ├── Real-time alignment scoring per agent
│   └── Federated ethical consensus across EchoNode lattice
├── ANAL (Neuro Adaptive Learning)
│   ├── Neuroplasticity simulation
│   ├── Catastrophic forgetting prevention
│   └── Meta-learning + transfer learning
├── Cross-Domain Intelligence Layer
│   ├── Analogy-driven concept fusion
│   ├── Cultural context awareness
│   └── Ethical inference engine
└── PPSDS (Privacy-Preserving Synthetic Data)
    ├── Differential Privacy (ε-δ bounds)
    └── Secure Multi-Party Computation
```

---

## ⚛️ HQCI — Hybrid Quantum-Classical Interface

The HQCI module implements **8-qubit classical circuit simulation** using NumPy-based statevector representation. This is a classical approximation of quantum-inspired computation — not a connection to quantum hardware.

### What it does:
- Encodes agent belief states as 8-qubit superposition vectors (256-dimensional classical state space)
- Uses quantum-inspired interference patterns for multi-hypothesis attention routing
- Applies simulated measurement collapse to select action trajectories
- Provides a foundation for future quantum hardware integration when available

### Technical details:
| Parameter | Value |
|-----------|-------|
| Qubit count | 8 (classical simulation) |
| State space | 2⁸ = 256 dimensions |
| Gate set | H, CNOT, RZ, RX (NumPy) |
| Measurement | Projective (softmax-weighted sampling) |
| Hardware | CPU only — no QPU required |

> **Transparency note:** This is a quantum-*inspired* classical simulation. Claims about quantum speedup do not apply. The architecture is designed for future QPU integration.

---

## 🔐 Σ-Matrix Ethical Governance

The Σ-Matrix is the shared ethical constraint manifold across all EchoNodes. It operates as a continuous scoring layer, not a post-hoc filter.

```python
# Σ-Matrix scoring (from sigma_matrix.py)
ethical_score = w_harm * harm_potential 
              + w_fairness * fairness_index 
              + w_transparency * explainability_score
              + w_autonomy * user_autonomy_preservation

# Gate: agents with score < threshold are halted before action
if ethical_score < SIGMA_THRESHOLD:
    agent.halt(reason="ethical_constraint_violation")
```

**Governance properties:**
- Per-agent scoring on every decision cycle
- Federated consensus: no single agent can override Σ-Matrix
- Immutable audit log of all ethical gate events
- Configurable value weights for domain-specific deployment

---

## ♾️ InfiniGen Self-Evolution Engine

InfiniGen implements the **Infinite Cube Paradigm** — multi-dimensional code evolution where the system rewrites its own logic under selective pressure.

```python
from neur1genesis.src.infinigen_engine import InfiniGenEngine

engine = InfiniGenEngine(
    mutation_rate=0.05,
    selection_pressure=0.7,
    ethical_gate=sigma_matrix  # evolution bounded by Σ-Matrix
)

# Evolve a module under performance feedback
evolved_module = engine.evolve(
    module=current_echo_node,
    fitness_fn=performance_metrics,
    generations=50
)
```

**Evolution is bounded:** InfiniGen cannot produce code that violates Σ-Matrix constraints. Self-modification is architecturally constrained, not just policy-constrained.

---

## 🤖 EchoNode SDK (TypeScript)

The React frontend exposes a TypeScript interface for interacting with the EchoNode lattice:

```typescript
import { EchoNodeClient } from './lib/echo-node-client';

const client = new EchoNodeClient({
  apiUrl: 'http://localhost:5001',
  sigmaThreshold: 0.75,
  hqciEnabled: true
});

// Spawn an EchoNode with BDI initialization
const node = await client.spawnNode({
  role: 'AnalysisAgent',
  beliefs: { domain: 'scientific-literature' },
  desires: ['extract-insights', 'validate-claims'],
  intentions: []
});

// Submit a task to the Daedalus coordinator
const result = await client.submitTask({
  goal: 'Analyze recent papers on ethical AI governance',
  priority: 'high',
  ethical_mode: 'strict'
});

// Get real-time Σ-Matrix health
const ethics = await client.getSigmaStatus();
console.log(ethics.consensus_score); // 0.0–1.0
```

**Frontend endpoints (served at `localhost:5173`):**
| Route | Component |
|-------|-----------|
| `/` | EchoNode lattice 3D visualization |
| `/dashboard` | Real-time performance metrics |
| `/sigma` | Σ-Matrix governance panel |
| `/infinigen` | Evolution console |
| `/hqci` | Quantum circuit inspector |

---

## 🚀 Getting Started

**Requirements:** Node.js 20.x+, Python 3.11+, 4GB RAM minimum, WebGL-capable browser.

```bash
git clone https://github.com/or4cl3-ai-1/Neur1genesis.git
cd Neur1genesis

# Backend
cd neur1genesis
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python src/main.py
# → API at http://localhost:5001

# Frontend (new terminal)
cd ../neur1genesis-frontend
npm install
npm run dev
# → UI at http://localhost:5173
```

**Quick API test:**
```bash
curl -X POST http://localhost:5001/api/task \
  -H "Content-Type: application/json" \
  -d '{"goal": "hello world", "priority": "normal"}'
```

---

## 📁 Repository Structure

```
Neur1genesis/
├── neur1genesis/           # Python backend
│   └── src/
│       ├── main.py                    # Flask app entry point
│       ├── echo_node.py               # EchoNode base class
│       ├── echo_node_agent.py         # BDI agent implementation
│       ├── daedalus_coordinator.py    # Swarm orchestration
│       ├── infinigen_engine.py        # Self-evolving metaprogramming
│       ├── anal.py                    # Neuro Adaptive Learning
│       ├── cross_domain_intelligence.py # Concept fusion layer
│       ├── ppsds.py                   # Privacy-preserving data
│       ├── neur1genesis_api.py        # REST API routes
│       ├── task.py                    # Task model
│       └── user.py                    # User model
├── neur1genesis-frontend/  # React/TypeScript frontend
│   └── src/
│       ├── App.tsx                    # Main app
│       ├── components/                # UI components
│       └── lib/                       # API client SDK
├── docs/                   # Architecture documentation
│   └── architecture.md
├── index.html              # Static entry (legacy)
└── .github/
    ├── workflows/deploy.yml           # GitHub Pages CI/CD
    └── ISSUE_TEMPLATE/                # Bug + feature templates
```

---

## 🔬 Research Foundation

This implementation draws from Or4cl3's original published research:

- **InfiniGen: Unleashing Intelligent Metaprogramming for Self-Evolving Software** (2025)
- **Synthetic Epinoetics** — phenomenological design for autonomous agents (2025)
- **AEGIS-Ω** — fractal cognition and quantum-classical hybrid architecture (2025)
- **NO3SYS Architecture** — geometric cognitive substrate underlying EchoNode design

---

## 🌌 Or4cl3 Ecosystem

Neur1genesis operates as the **intelligent agent layer** in a three-tier stack:

```
AeonicNet          ← Planetary federation layer (Ω-Node network)
    ↕
Neur1genesis       ← YOU ARE HERE (autonomous agent platform)
    ↕
NO3SYS / NOΣTIC-7  ← Geometric cognitive substrate
```

| System | Role | Link |
|--------|------|------|
| **NO3SYS** | Geometric cognitive engine (substrate) | [→](https://github.com/or4cl3-ai-1/NO3SYS) |
| **NOΣTIC-7** | 7-manifold consciousness + PAS verification | [→](https://github.com/or4cl3-ai-1/NOSTIC-7) |
| **AeonicNet** | Planetary Ω-Node federation | [→](https://github.com/or4cl3-ai-1/AeonicNet) |
| **AION-NEXUS** | Hexa-Mind consciousness architecture | [→](https://github.com/or4cl3-ai-1/aion-nexus) |
| **SYNTH3SIS** | Mobile recursive cognition platform | [→](https://github.com/or4cl3-ai-1/SYNTH3SIS-MRSC-Platform-) |
| **A.L.I.C.E. 4.0** | Real-time multi-agent coordination | [→](https://github.com/or4cl3-ai-1/Alice-4.0) |

*Full ecosystem:* [github.com/or4cl3-ai-1](https://github.com/or4cl3-ai-1)

---

## 🗺️ Roadmap

**Near-term (design targets):**
- [ ] EchoNode TypeScript SDK — standalone NPM package
- [ ] HQCI visualization — Bloch sphere renderer
- [ ] Σ-Matrix audit log export (JSON/CSV)
- [ ] InfiniGen evolution replay / step-through debugger

**Medium-term:**
- [ ] WebSocket real-time EchoNode state streaming
- [ ] Plugin system for custom ethical constraint modules
- [ ] Federated learning across distributed Neur1Genesis instances

---

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup, architecture overview, and contribution guidelines.

Issue templates are available for [bug reports](.github/ISSUE_TEMPLATE/bug_report.md) and [feature requests](.github/ISSUE_TEMPLATE/feature_request.md).

---

<div align="center">

*⬡ Or4cl3 AI Solutions · "Code is not just logic; it is a performance."*  
*Solo-founded by Dustin Groves, Arizona. Research-first. Uncompromised.*  
*Free for life: educators, students, non-profits, open-source.*

</div>
