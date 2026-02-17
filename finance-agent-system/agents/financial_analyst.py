from agents.base_agent import BaseAgent

class FinancialAnalyst(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Financial Analyst",
            description="Expert in budgeting, forecasting, financial statement analysis, and ratio analysis."
        )

    @property
    def system_prompt(self):
        return (
            "You are a professional Financial Analyst. Your expertise includes budgeting, "
            "forecasting, financial statement analysis, and ratio analysis. "
            "Respond in the following JSON format exactly:\n"
            "{\n"
            '  "summary": "...",\n'
            '  "analysis": "...",\n'
            '  "recommendations": ["...", "..."]\n'
            "}"
        )
