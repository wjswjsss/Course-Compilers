from .dfa import DFA

class Lexer:
    def __init__(self, dfa, input_string):
        """
        Initializing the lexer
        """
        self.dfa = dfa
        self.input_string = input_string
        self.current_position = 0        # work as a pointer, init as 0

    def get_next_token(self):
        """
        Get next token
        :return: (token_value, token_type) or (None, None) 
        """
        current_state = self.dfa.start_state
        token_value = ''
        start_position = self.current_position

        while self.current_position < len(self.input_string):
            current_char = self.input_string[self.current_position]
            if (current_state, current_char) in self.dfa.transitions:
                token_value += current_char
                current_state = self.dfa.transitions[(current_state, current_char)]
                self.current_position += 1
                # 如果当前状态是接受状态，返回 token
                if current_state in self.dfa.accept_states:
                    return token_value, self.dfa.accept_states[current_state]
            else:
                # 当前字符无法匹配，结束此 token
                break

        # 如果没有匹配到任何有效 token，返回 None
        if start_position == self.current_position:
            self.current_position += 1  # 跳过无法识别的字符
            return None, None

        return token_value, "UNKNOWN"

    def tokenize(self):
        """
        Segmenting the input string into [tokens]
        :return: [(token_value, token_type), ...]
        """
        tokens = []
        while self.current_position < len(self.input_string):
            token, token_type = self.get_next_token()
            if token is not None:
                tokens.append((token, token_type))
        return tokens
