class TuringMachine:
    def __init__(self, rules: dict):
        self.tape = ['_']
        self.head = 0
        self.state = 'q0'
        self.rules = rules
    
    def step(self):
        current_symbol = self.tape[self.head] if self.head < len(self.tape) else '_'
        rule = self.rules.get((self.state, current_symbol))
        
        if not rule:
            return False
            
        new_state, write, move = rule
        if self.head < len(self.tape):
            self.tape[self.head] = write
        else:
            self.tape.append(write)
            
        self.head += 1 if move == 'R' else -1
        self.state = new_state
        return True