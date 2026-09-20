import streamlit as st

# --- BANCO DE DADOS PCDT FICTÍCIO (EXEMPLO) ---
PCDT_DATABASE = {
    "cardiologia": {
        "criterios_urgencia": ["dor torácica", "dispneia aguda", "síncope", "pressão arterial sistólica > 180"],
        "prazo_máximo_horas": 2
    },
    "neurologia": {
        "criterios_urgencia": ["déficit motor súbito", "confusão mental aguda", "cefaleia intensa súbita"],
        "prazo_máximo_horas": 1
    }
}

def sanitizar_dados(texto: str) -> str:
    # Remove espaços excedentes e formata o texto básico
    return texto.strip()

# --- AGENTE DE TRIAGEM INTELIGENTE ---
def agente_triagem(especialidade: str, caso_clínico: str):
    """
    Analisa o caso clínico com base nos PCDTs cadastrados e atribui criticidade.
    """
    caso_sanitizado = sanitizar_dados(caso_clínico)
    caso_lower = caso_sanitizado.lower()
    
    dados_pcdt = PCDT_DATABASE.get(especialidade.lower(), {"criterios_urgencia": [], "prazo_máximo_horas": 24})
    
    urgente = any(criterio in caso_lower for criterio in dados_pcdt["criterios_urgencia"])
    
    if urgente:
        return {
            "status": "ALTA PRIORIDADE (VERMELHO)",
            "prazo": f"Atendimento imediato em até {dados_pcdt['prazo_máximo_horas']} horas.",
            "caso_sanitizado": caso_sanitizado
        }
    else:
        return {
            "status": "ELETIVO / AMBULATORIAL (VERDE/AMARELO)",
            "prazo": "Encaminhado para regulação regular conforme fila padrão.",
            "caso_sanitizado": caso_sanitizado
        }

# --- INTERFACE GRÁFICA PRINCIPAL ---
def principal():
    st.title("Plataforma RegulaMed - Governança e Regulação em Saúde")
    st.markdown("**Motor de Inteligência Artificial Agentiva para otimização de Processos no SUS**")
    st.divider()
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subtitle("📥 Entrada de Solicitação de Regulação")
        especialidade = st.selectbox("Especialidade Médica", ["Cardiologia", "Neurologia", "Ortopedia", "Dermatologia"])
        caso_clínico = st.text_area("Descrição do Caso Clínico", placeholder="Descreva os sintomas, histórico e queixa principal do paciente...")
        
        if st.button("Executar Triagem IA"):
            if caso_clínico.strip():
                with st.spinner("Analisando PCDTs e criticidade..."):
                    resultado = agente_triagem(especialidade, caso_clínico)
                    
                    st.success("Triagem realizada com sucesso!")
                    st.write(f"**Status:** {resultado['status']}")
                    st.write(f"**Prazo Sugerido:** {resultado['prazo']}")
                    st.write(f"**Caso Sanitizado:** {resultado['caso_sanitizado']}")
            else:
                st.warning("Por favor, preencha a descrição do caso clínico antes de executar.")

if __name__ == "__main__":
    principal()
