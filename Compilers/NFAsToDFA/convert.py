from dfa_and_nfa import DFA, NFA

def epsilon_closure(states, transitions):
    """Compute the epsilon closure of a set of states."""
    stack = list(states) # Initialize the stack with all the states we already have
    closure = set(states) # The closure is at least contains the initial states

    while stack: # while the stack is not empty, we loop ...
        state = stack.pop()
        if (state, '') in transitions:  # '' represents epsilon transitions
            for next_state in transitions[(state, '')]:
                if next_state not in closure:
                    closure.add(next_state)
                    stack.append(next_state) # We got to come back
    
    return closure

def move(states, symbol, transitions):
    """Find the set of states reachable from 'states' on input 'symbol'."""
    reachable_states = set()
    for state in states:
        if (state, symbol) in transitions:
            reachable_states.update(transitions[(state, symbol)])
    
    return reachable_states

def convert_nfa_to_dfa(nfa):
    dfa = DFA()  # Create a new DFA object

    # Start state of DFA is epsilon-closure of NFA's start state
    initial_state = frozenset(epsilon_closure({nfa.start_state}, nfa.transitions))
    dfa.start_state = initial_state
    unmarked_states = [initial_state]  # List of unmarked DFA states
    dfa.states.append(initial_state)
    
    """Check if the initial state is a final state in DFA"""
    if any(state in nfa.final_states for state in initial_state):
            dfa.final_states.add(initial_state) # Add to the DFA's final_states{}

    while unmarked_states:
        T = unmarked_states.pop(0)  # Get an unmarked state
        
        for a in nfa.alphabet:  # For each input symbol
            U = frozenset(epsilon_closure(move(T, a, nfa.transitions), nfa.transitions))  # Calculate the new DFA state

            if U and U not in dfa.states:  # If U is a new state AND U is NOT an empty set
                dfa.states.append(U)  # Add U to the DFA states
                unmarked_states.append(U)  # Mark it unmarked

                """Check if any of the NFA's final state is in U"""
                if any(state in nfa.final_states for state in U):
                    dfa.final_states.add(U)
            
            # Add the transition for T on symbol a to U
            if U: # Only if U is not an empty set
                dfa.transitions[(T, a)] = U

    return dfa
