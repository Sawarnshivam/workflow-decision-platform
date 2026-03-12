from rules.base_rule import BaseRule
from external.credit_service import CreditService
import time


class CreditRule(BaseRule):

    def __init__(self):
        self.credit_service = CreditService()

    def evaluate(self, data):

        user_id = data.get("request_id")

        retries = 3

        for attempt in range(retries):

            try:

                response = self.credit_service.get_credit_score(user_id)

                score = response["credit_score"]

                if score >= 600:
                    return {"rule": "credit_rule", "result": "PASS", "score": score}

                return {"rule": "credit_rule", "result": "FAIL", "score": score}

            except Exception:

                time.sleep(1)

        return {"rule": "credit_rule", "result": "FAIL", "reason": "service_failure"}