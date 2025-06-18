def test_basic_match():
    engine = RegexEngine("basic")
    assert engine.match_current_line("this is a basic test")

def test_no_match():
    engine = RegexEngine("no-basic")
    assert engine.match_current_line("this is not a basic test")

def test_empty_pattern():
    engine = RegexEngine("")
    assert engine.match_current_line("I think it is a match")

def test_exact_match():
    engine = RegexEngine("basic")
    assert engine.match_current_line("this is another basic test")