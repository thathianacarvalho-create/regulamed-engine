# Regulamed-Engine 🇧🇷 🇬🇧

**[PT]** Motor de Inteligência Artificial Agentiva e Governança para Otimização de Processos de Regulação em Saúde no SUS. Focado em eliminar gargalos burocráticos, garantir conformidade clínica (PCDT) e assegurar privacidade estrita de dados (LGPD/HIPAA).

**[EN]** Agentic AI & Governance Engine for Healthcare Regulation Optimization in Public Health Systems (SUS). Focused on eliminating bureaucratic bottlenecks, ensuring clinical compliance (PCDT/Guidelines), and enforcing strict data privacy (LGPD/HIPAA).

---

## 🚀 Key Features / Principais Funcionalidades

- **[PT] Sanitização de Dados na Origem:** Anonimização automática de PII/PHI para conformidade com LGPD.
- **[EN] Edge Data Sanitization:** Automated PII/PHI anonymization ensuring strict compliance.
- **[PT] Triagem Baseada em Agentes:** Automação inteligente do fluxo de triagem de leitos e exames de alta complexidade.
- **[EN] Agentic Triage:** Intelligent workflow automation for hospital bed and complex exam routing.
- **[PT] Guardrails Determinísticos:** Travas lógicas em Python para evitar alucinações de IA e garantir rigor técnico.
- **[EN] Deterministic Guardrails:** Python-based logic layers preventing AI hallucinations and enforcing safety.
- **[PT] Auditoria e RAG:** Conexão segura com protocolos oficiais do Ministério da Saúde.
- **[EN] Auditability & RAG:** Secure integration with official medical guidelines and protocols.

---

## 🛠️ System Architecture / Arquitetura do Sistema

```text
regulamed-engine/
│
├── data/                  # Official Clinical Guidelines & Knowledge Base (PCDT)
├── src/                   # Source Code
│   ├── agents/            # Autonomous Triage Agents
│   ├── guardrails/        # Deterministic Security & Completeness Rules
│   ├── privacy/           # Data Sanitization & LGPD Compliance Modules
│   └── app.py             # Streamlit Audit-Ready Interface
│
├── requirements.txt       # Project Dependencies
└── README.md              # Documentation (PT/EN)
