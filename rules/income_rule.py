from rules.base_rule import BaseRule

class IncomeRule(BaseRule):
    def evaluate(self, data):
        income = data.get("income", 0)

        if income >= 50000:
            return {"rule": "income_rule", "result": "PASS"}

        return {"rule": "income_rule", "result": "FAIL"}