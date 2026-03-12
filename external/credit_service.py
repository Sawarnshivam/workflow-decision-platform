import random


class CreditService:

    def get_credit_score(self, user_id):

        # simulate occasional service failure
        if random.random() < 0.3:
            raise Exception("Credit Service Unavailable")

        score = random.randint(300, 900)

        return {
            "user_id": user_id,
            "credit_score": score
        }