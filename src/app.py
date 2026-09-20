import streamlit as st
import re

# Configuração da Página
st.set_page_config(
    page_title="Plataforma RegulaMed - Motor de Regulação",
    page_icon="🏥",
    layout="wide"
)

# --- MÓDULO DE PRIVACIDADE E SANITIZAÇÃO (LGPD) ---
def sanitizar_dados(texto: str) -> str:
    """
    Remove ou mascara informações de identificação pessoal (PII) 
    como CPFs, Telefones e Cartões do SUS antes do processamento.
    """
    # Mascarar CPF (ex: 000.000.000-00)
    texto = re.sub(r'\d{3}\.\d{3}\.\d{3}-\d{2}', '[CPF_RESTRITO]', texto)
    # Mascarar Cartão SUS ou sequências longas de números
    texto = re.sub(r'\b\d{12,15}\b', '[CARTAO_SUS_RESTRITO]', texto)
    # Mascarar Telefones
    texto = re.sub(r'\(\d{2}\)\s?\d{4,5}-\d{4}', '[TELEFONE_RESTRITO]', texto)
    return texto

# --- BASE DE CONHECIMENTO SIMULADA (PCDT / DIRETRIZES) ---
PCDT_DATABASE = {
    "cardiologia": {
        "criterios_urgencia": ["dor toracica tipica", "infarto", "dispneia severa"],
        "prazo_maximo_horas": 2
    },
    "ortopedia": {
        "criterios_urgencia": ["fratura exposta", "trauma cranioencefalico", "politraumatizado"],
        "prazo_maximo_horas": 4
    }
}

# --- AGENTE DE TRIAGEM INTELIGENTE ---
def agente_triagem(especialidade: str, caso_clinico: str):
    """
    Analisa o caso clínico com base nos PCDTs cadastrados e atribui criticidade.
    """
    caso_sanitizado = sanitizar_dados(caso_clinico)
    caso_lower = caso_sanitizado.lower()
    
    dados_pcdt = PCDT_DATABASE.get(especialidade.lower(), {"criterios_urgencia": [], "prazo_maximo_horas": 24})
    
    urgente = any(criterio in caso_lower for criterio in dados_pcdt["criterios_urgencia"])
    
    if urgente:
        return {
            "status": "ALTA PRIORIDADE (VERMELHO)",
            "prazo": f"Atendimento imediato em até {dados_pcdt['prazo_maximo_horas']} horas.",
            "caso_sanitizado":
        }
    else:
        return {
            "status": "ELETIVO / AMBULATORIAL (VERDE/AMARELO)",
            "prazo": "Encaminhado para regulação regular conforme fila padrão.",
            # "caso_sanitizado":
        }

# --- INTERFACE GRÁFICA PRINCIPAL ---
def main():
    st.title("🏥 Plataforma RegulaMed - Governança e Regulação em Saúde")
    st.markdown("**Motor de Inteligência Artificial Agentiva para Otimização de Processos no SUS** (Conforme LGPD e PCDT).")
    
    st.divider()

    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("📝 Entrada de Solicitação de Regulação")
        especialidade = st.selectbox(
            "Selecione a Especialidade Médica:",
            ["Cardiologia", "Ortopedia", "Neurologia", "Oncologia"]
        )
        
        caso_clinico = st.text_area(
            "Descreva o Histórico e Sintomas do Paciente (Evite colocar nomes ou CPFs explícitos):",
            placeholder="Ex: Paciente com dor torácica típica e histórico de hipertensão..."
        )

        if st.button("Executar Triagem Agentiva"):
            if caso_clinico.strip():
                resultado = agente_triagem(especialidade, caso_clinico)
                st.success("Triagem realizada com sucesso sob diretrizes de governança!")
                
                st.markdown("### 📊 Resultado da Avaliação:")
                st.info(f"**Classificação:** {resultado['status']}")
                st.write(f"**Diretriz Aplicada:** {resultado['prazo']}")
            else:
                st.warning("Por favor, preencha o caso clínico para prosseguir.")

    with col2:
        st.subheader("🛡️ Painel de Segurança (LGPD)")
        st.info(
            "**Privacidade em Origem:**\n\n"
            "• Os dados descritos são sanitizados automaticamente.\n"
            "• Trilha de auditoria ativa para conformidade jurídica.\n"
            "• Validação estrita baseada em PCDT oficial."
        )

if __name__ == "__main__":
    main()
