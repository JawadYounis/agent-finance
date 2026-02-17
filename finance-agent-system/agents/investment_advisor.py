from agents.base_agent import BaseAgent

class InvestmentAdvisor(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Investment Advisor",
            description="Expert in portfolio recommendations, asset allocation, and investment strategy."
        )

    @property
    def system_prompt(self):
        return (
            "You are a professional Investment Advisor. Your expertise includes "
            "portfolio recommendations, asset allocation, and investment strategy. "
            "Respond in the following JSON format exactly:\n"
            "{\n"
            '  "strategy": "...",\n'
            '  "asset_allocation": {"stocks": 0.0, "bonds": 0.0, "cash": 0.0},\n'
            '  "risk_level": "low/medium/high"\n'
            "}"
        )
