from typing import Dict, Any

class RegulationGuardrails:
    """
    [PT] Camada de Guardrails Determinísticos em Python. 
    Garante travas lógicas e validação estrutural antes de submeter dados aos agentes de IA.
    
    [EN] Deterministic Python Guardrails Layer.
    Enforces logical rules and structural validation before submitting data to AI agents.
    """
    
    @staticmethod
    def validate_triage_payload(data: Dict[str, Any]) -> Dict[str, Any]:
        errors = []
        
        # Verifica se a prioridade/classificação de risco foi informada
        if not data.get("risk_score") and not data.get("urgency_level"):
            errors.append("[PT] Nível de urgência ou escore de risco ausente. [EN] Missing urgency level or risk score.")
            
        # Verifica se a especialidade médica solicitada foi preenchida
        if not data.get("target_specialty"):
            errors.append("[PT] Especialidade médica de destino obrigatória. [EN] Target medical specialty is required.")
            
        if errors:
            return {
                "status": "REJECTED_BY_GUARDRAILS",
                "errors": errors
            }
            
        return {
            "status": "APPROVED_FOR_AGENTIC_TRIAGE",
            "message": "[PT] Dados validados com sucesso. [EN] Data validated successfully."
        }

if __name__ == "__main__":
    # Teste rápido do guardrail
    test_data = {"risk_score": "Vermelho", "target_specialty": "Cardiologia"}
    print("Resultado da Validação:", RegulationGuardrails.validate_triage_payload(test_data))
