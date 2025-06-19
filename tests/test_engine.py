import unittest
from line_watch.engine import RegexEngine

class TestRegexEngine(unittest.TestCase):
    def test_basic_match(self):
        engine = RegexEngine("basic")
        self.assertTrue(engine.match_current_line("this is a basic test"))

    def test_no_match(self):
        engine = RegexEngine("no-basic")
        self.assertTrue(engine.match_current_line("this is not a basic test"))

    def test_empty_pattern(self):
        engine = RegexEngine("")
        self.assertTrue(engine.match_current_line("I think it is a match"))

    def test_exact_match(self):
        engine = RegexEngine("basic")
        self.assertTrue(engine.match_current_line("this is another basic test"))

    def test_wildcard_match(self):
        engine = RegexEngine("a.c")
        self.assertTrue(engine.match_at_position("a9c"), 0)

if __name__ == "__main__":
    unittest.main()