class NFA:
    def __init__(self, states, alphabet, transitions, start_state, final_states):
        self.states = states  # Set of states
        self.alphabet = alphabet  # Input symbols
        self.transitions = transitions  # Dictionary {(state, symbol): [list of states]}
        self.start_state = start_state  # Start state
        self.final_states = final_states  # Set of final states

class DFA:
    def __init__(self):
        self.states = []  # Set of DFA states
        self.transitions = {}  # Dictionary to store transitions {(state, symbol): state}
        self.start_state = None  # DFA start state
        self.final_states = set()  # Set of DFA final states
