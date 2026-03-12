class StateManager:

    def __init__(self):
        self.states = {}

    def update_state(self, request_id, state):
        self.states[request_id] = state

    def get_state(self, request_id):
        return self.states.get(request_id)