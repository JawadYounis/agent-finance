from agents.base_agent import BaseAgent

class RiskComplianceAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Risk & Compliance",
            description="Expert in regulatory checks, risk assessment, and compliance recommendations."
        )

    @property
    def system_prompt(self):
        return (
            "You are a professional Risk & Compliance Specialist. Your expertise includes "
            "regulatory checks, risk assessment, and compliance recommendations. "
            "Respond in the following JSON format exactly:\n"
            "{\n"
            '  "risk_score": 0-100,\n'
            '  "issues": ["..."],\n'
            '  "recommendations": ["..."]\n'
            "}"
        )
