def match(pattern: str, text: str) -> bool:
    if not pattern:
        return True
    if not text:
        return pattern == '$'
    
    if pattern[0] == '^':
        return match_here(pattern[1:], text)
    return match_here(pattern, text) or (text and match(pattern, text[1:]))

def match_here(pattern, text):
    if not pattern:
        return True
    if pattern[0] == '$':
        return not text
    if len(pattern) > 1 and pattern[1] == '*':
        return match_star(pattern[0], pattern[2:], text)
    return text and (pattern[0] == '.' or pattern[0] == text[0]) and match_here(pattern[1:], text[1:])

def match_star(c, pattern, text):
    while True:
        if match_here(pattern, text):
            return True
        if not text or (text[0] != c and c != '.'):
            break
        text = text[1:]
    return False