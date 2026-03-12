from rules.income_rule import IncomeRule
from rules.duplicate_rule import DuplicateRule
from rules.credit_rule import CreditRule


class RuleEngine:

    def __init__(self):
        self.rules = [
            IncomeRule(),
            DuplicateRule(),
            CreditRule()
        ]

    def evaluate_rules(self, data):

        results = []

        for rule in self.rules:
            result = rule.evaluate(data)
            results.append(result)

        return results