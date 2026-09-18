import streamlit as st
import sys
import os

# Adiciona o diretório raiz ao path para importar os módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.privacy.sanitizer import DataSanitizer
from src.guardrails.rules import RegulationGuardrails
from src.agents.triage_agent import TriageAgent

st.set_page_config(
    page_title="Regulamed-Engine - SUS",
    page_icon="🇧🇷",
    layout="wide"
)

st.title("Regulamed-Engine 🇧🇷 🇬🇧")
st.markdown("### Motor de IA Agentiva e Governança para Regulação em Saúde no SUS")
st.markdown("*Agentic AI & Governance Engine for SUS Healthcare Regulation Optimization*")

st.divider()

# Formulário de entrada na interface
st.subheader("📝 Dados do Pedido de Regulação / Triage Request")

with st.form("triage_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        patient_raw_text = st.text_area(
            "Texto Clínico com Dados do Paciente (Simula prontuário com PII/PHI)",
            value="Paciente Maria Souza, CPF 123.456.789-00, Cartão SUS 987654321098765, necessita de regulação urgente para Cardiologia devido a dor torácica aguda."
        )
        
    with col2:
        target_specialty = st.selectbox(
            "Especialidade Médica de Destino / Target Specialty",
            ["Cardiologia", "Neurologia", "Ortopedia", "Oncologia", "UTI Geral"]
        )
        urgency_level = st.selectbox(
            "Nível de Urgência / Risk Score",
            ["Vermelho (Emergência)", "Amarelo (Urgente)", "Verde (Eletivo)"]
        )
        
    submitted = st.form_submit_button("Executar Triagem Segura / Run Secure Triage")

if submitted:
    st.divider()
    st.subheader("🔍 Resultados do Pipeline de Governança")
    
    # 1. Passo de Sanitização (LGPD/HIPAA)
    sanitized_text = DataSanitizer.anonymize_text(patient_raw_text)
    st.markdown("#### 1. LGPD/HIPAA Sanitization Layer")
    st.success("Dados PII/PHI anonimizados com sucesso na origem.")
    st.code(sanitized_text, language="text")
    
    # 2. Passo de Guardrails Determinísticos
    payload = {
        "risk_score": urgency_level,
        "target_specialty": target_specialty,
        "sanitized_content": sanitized_text
    }
    
    guardrail_result = RegulationGuardrails.validate_triage_payload(payload)
    st.markdown("#### 2. Deterministic Guardrails Layer")
    
    if guardrail_result["status"] == "APPROVED_FOR_AGENTIC_TRIAGE":
        st.success(guardrail_result["message"])
        
        # 3. Passo de Agente de IA
        agent = TriageAgent()
        agent_result = agent.process_triage(payload)
        
        st.markdown("#### 3. Agentic Triage Layer (SUS PCDT)")
        st.json(agent_result)
    else:
        st.error("Validação bloqueada pelos Guardrails:")
        st.write(guardrail_result["errors"])
