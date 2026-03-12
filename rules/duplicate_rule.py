from rules.base_rule import BaseRule

class DuplicateRule(BaseRule):
    def evaluate(self, data):

        if data.get("is_duplicate"):
            return {"rule": "duplicate_rule", "result": "FAIL"}

        return {"rule": "duplicate_rule", "result": "PASS"}