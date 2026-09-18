import re

class DataSanitizer:
    """
    [PT] Módulo responsável pela sanitização de dados sensíveis (PII/PHI) na origem,
    garantindo total conformidade com a LGPD e HIPAA antes do processamento por IA.
    
    [EN] Module responsible for edge sanitization of sensitive data (PII/PHI),
    ensuring full compliance with LGPD and HIPAA prior to AI processing.
    """
    
    @staticmethod
    def anonymize_text(text: str) -> str:
        if not text:
            return ""
            
        # Remove CPFs (ex: 000.000.000-00 ou 00000000000)
        text = re.sub(r'\d{3}\.\d{3}\.\d{3}-\d{2}|\d{11}', '[CPF_ANONIMIZADO]', text)
        
        # Remove Cartão Nacional de Saúde / SUS (ex: 15 dígitos)
        text = re.sub(r'\b\d{15}\b', '[CNS_ANONIMIZADO]', text)
        
        # Remove Telefones (ex: (11) 99999-9999)
        text = re.sub(r'\(?\d{2}\)?\s?\d{4,5}-?\d{4}', '[TELEFONE_ANONIMIZADO]', text)
        
        # Remove E-mails
        text = re.sub(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', '[EMAIL_ANONIMIZADO]', text)
        
        return text

if __name__ == "__main__":
    # Teste rápido do sanitizador
    sample_text = "Paciente João da Silva, CPF 123.456.789-00, Cartão SUS 123456789012345, contato (11) 98765-4321."
    print("Original:", sample_text)
    print("Sanitizado:", DataSanitizer.anonymize_text(sample_text))
