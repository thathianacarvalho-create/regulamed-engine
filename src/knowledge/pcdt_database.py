from typing import Dict, Any

class PCDTKapowDatabase:
    """
    [PT] Base de Conhecimento Estruturada com Protocolos Clínicos, Diretrizes Terapêuticas (PCDT) do SUS,
    diretrizes de sociedades médicas (ex: SBC, Febrasgo, SBP) e regras do Sistema de Regulação (SISREG).
    [EN] Structured Knowledge Base with SUS Clinical Protocols, Therapeutic Guidelines (PCDT),
    medical society guidelines (e.g., SBC, Febrasgo, SBP), and Regulation System (SISREG) rules.
    """
    
    GUIDELINES: Dict[str, Dict[str, Any]] = {
        "Cardiologia": {
            "condition": "Acute Chest Pain / Acute Coronary Syndrome",
            "required_exams": ["Electrocardiogram (ECG) within 10 min", "Myocardial necrosis markers"],
            "sus_regulation_priority": "Red - Zero Slot / Immediate Regulation",
            "legal_framework": "GM/MS Ordinance No. 1.600/2011 & Brazilian Society of Cardiology (SBC) Guidelines"
        },
        "Neurologia": {
            "condition": "Acute Stroke (CVA)",
            "required_exams": ["Non-contrast Brain Computed Tomography (CT)", "NIHSS Neurological Assessment"],
            "sus_regulation_priority": "Red - Strict Door-to-Needle Time Protocol",
            "legal_framework": "National Stroke Care Guidelines & SUS Protocols"
        },
        "Clinica Cirurgica": {
            "condition": "Acute Abdomen / Urgent Surgical Conditions",
            "required_exams": ["Complete blood count", "Abdominal imaging (Ultrasound/CT)", "Risk assessment"],
            "sus_regulation_priority": "Yellow/Red - Priority Surgical Regulation via SISREG",
            "legal_framework": "SUS Elective and Emergency Surgery Regulation Guidelines"
        },
        "Oncologia": {
            "condition": "Suspected Malignant Neoplasm (Oncology Priority)",
            "required_exams": ["Histopathological biopsy report", "Imaging staging"],
            "sus_regulation_priority": "Red - Legal 60-Day Deadline Compliance (Law No. 12.732/2012)",
            "legal_framework": "Law No. 12.732/2012 (60-Day Law for First Oncology Treatment)"
        },
        "Ortopedia": {
            "condition": "Acute Trauma / Complex Fracture",
            "required_exams": ["Orthopedic X-ray series", "Vascular-nervous evaluation"],
            "sus_regulation_priority": "Yellow/Red - Traumatology Regulation Network",
            "legal_framework": "National Trauma and Orthopedic Care Network Protocols"
        },
        "Pediatria": {
            "condition": "Acute Respiratory Distress / Pediatric Emergency / Severe Dehydration",
            "required_exams": ["Pulse oximetry", "Pediatric assessment triangle (PAT)", "Glycemia"],
            "sus_regulation_priority": "Red - Pediatric Urgency Network / Immediate Bed Regulation",
            "legal_framework": "Ministry of Health Pediatric Emergency Guidelines & SBP Protocols"
        },
        "Ginecologia e Obstetricia": {
            "condition": "Obstetric Emergency / Severe Preeclampsia / Labor Complications",
            "required_exams": ["Obstetric Ultrasound", "Cardiotocography (CTG)", "Proteinuria evaluation / Blood pressure monitoring"],
            "sus_regulation_priority": "Red - Rede Cegonha / Immediate Obstetric Regulation (Zero Tolerance for Maternal Mortality)",
            "legal_framework": "Rede Cegonha Guidelines & Febrasgo Emergency Protocols"
        }
    }

    @classmethod
    def get_protocol(cls, specialty: str) -> Dict[str, Any]:
        """
        [PT] Recupera o protocolo oficial e diretrizes regulatórias para a especialidade solicitada.
        [EN] Retrieves the official protocol and regulatory guidelines for the requested specialty.
        """
        return cls.GUIDELines.get(specialty, {
            "condition": "General Outpatient Regulation / Elective Care",
            "required_exams": ["Primary Health Care (UBS) basic clinical evaluation"],
            "sus_regulation_priority": "Yellow/Green - SISREG Regulated Queue",
            "legal_framework": "National SUS Regulation Directives"
        })

if __name__ == "__main__":
    print("Obstetrics Protocol Test:", PCDTKapowDatabase.get_protocol("Ginecologia e Obstetricia"))
