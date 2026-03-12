class BaseRule:
    def evaluate(self, data):
        raise NotImplementedError("Rule must implement evaluate method")