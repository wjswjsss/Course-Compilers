def move(states, symbol, transitions):
    """Find the set of states reachable from 'states' on input 'symbol'."""
    reachable_states = set()
    for state in states:
        if (state, symbol) in transitions:
            reachable_states.update(transitions[(state, symbol)])
    
    return reachable_states