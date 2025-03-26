from src.turing_machine import TuringMachine

def test_binary_increment():
    rules = {
        ('q0', '1'): ('q0', '1', 'R'),
        ('q0', '0'): ('q0', '0', 'R'),
        ('q0', '_'): ('q1', '_', 'L'),
        ('q1', '0'): ('qf', '1', 'S'),
        ('q1', '1'): ('q1', '0', 'L'),
        ('q1', '_'): ('qf', '1', 'S')
    }
    
    tm = TuringMachine(rules)
    tm.tape = ['1', '0', '1', '1']  # 1011 (11 en binario)
    
    while tm.step():
        pass
    
    assert tm.tape[:4] == ['1', '1', '0', '0']  # 1100 (12 en binario)