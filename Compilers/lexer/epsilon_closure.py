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