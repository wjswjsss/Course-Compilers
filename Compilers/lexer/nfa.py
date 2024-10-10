class NFA:
    def __init__(self, states, alphabet, transitions, start_state, final_states):
        self.states = states  # Set of states
        self.alphabet = alphabet  # Input symbols
        self.transitions = transitions  # Dictionary {(state, symbol): [list of states]}
        self.start_state = start_state  # Start state
        self.final_states = final_states  # Set of final states