class DFA:
    def __init__(self):
        self.states = []  # Set of DFA states
        self.transitions = {}  # Dictionary to store transitions {(state, symbol): state}
        self.start_state = None  # DFA start state
        self.final_states = set()  # Set of DFA final states