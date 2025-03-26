from src.regex_engine import match

def test_regex_basics():
    assert match("a", "a") is True
    assert match("a", "b") is False
    assert match("a*", "aaa") is True
    assert match("^a.*c$", "abc") is True
    assert match("a.*b", "acb") is True