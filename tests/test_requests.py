from engine.decision_engine import DecisionEngine


engine = DecisionEngine()


def test_success_case():

    request = {
        "request_id": 1,
        "income": 80000,
        "is_duplicate": False
    }

    result = engine.process_request(1, request)

    print("\nSUCCESS CASE:", result)


def test_low_income():

    request = {
        "request_id": 2,
        "income": 20000,
        "is_duplicate": False
    }

    result = engine.process_request(2, request)

    print("\nLOW INCOME CASE:", result)


def test_duplicate_request():

    request = {
        "request_id": 3,
        "income": 80000,
        "is_duplicate": True
    }

    result = engine.process_request(3, request)

    print("\nDUPLICATE CASE:", result)


def test_external_failure():

    request = {
        "request_id": 4,
        "income": 80000,
        "is_duplicate": False
    }

    result = engine.process_request(4, request)

    print("\nEXTERNAL SERVICE TEST:", result)


if __name__ == "__main__":

    test_success_case()
    test_low_income()
    test_duplicate_request()
    test_external_failure()