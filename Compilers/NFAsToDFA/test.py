"""
Hi, ... good morning, good afternoon and good night...
                                                                    Jiashu @NEUQ
                                                                    Oct 3th, 2024
"""

from colorama import Fore               # Colorize the output text on the console
from dfa_and_nfa import NFA, DFA
from convert import convert_nfa_to_dfa

# Example NFA
states = {'q0', 'q1', 'q2'}
alphabet = {'a', 'b'}
transitions = {
    ('q0', 'a'): ['q1'],
    ('q1', 'b'): ['q2'],
    ('q0', ''): ['q2']  # Epsilon transition from q0 to q2
}
start_state = 'q0'
final_states = {'q2'}

nfa = NFA(states, alphabet, transitions, start_state, final_states)

# Convert
dfa = convert_nfa_to_dfa(nfa)

# Print
print(Fore.BLUE + "-"*80)
print(Fore.RED + "Hi, nice to meet you!")
print(Fore.CYAN + "DFA States:", Fore.GREEN + str(dfa.states))
print(Fore.CYAN + "DFA Start State:", Fore.GREEN + str(dfa.start_state))
print(Fore.CYAN + "DFA Transitions:")
for (state, symbol), target_state in dfa.transitions.items():
    print(Fore.YELLOW + f"  From {state} on '{symbol}' -> {target_state}")
print(Fore.CYAN + "DFA Final States:", Fore.GREEN + str(dfa.final_states))
