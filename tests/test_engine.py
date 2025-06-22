import unittest
from line_watch.engine import RegexEngine

class TestRegexEngine(unittest.TestCase):
    def test_basic_match(self):
        engine = RegexEngine("basic")
        self.assertTrue(engine.match_current_line("this is a basic test"))

    def test_no_match(self):
        engine = RegexEngine("no-basic")
        self.assertFalse(engine.match_current_line("this is not a basic test"))

    def test_empty_pattern(self):
        engine = RegexEngine("")
        self.assertTrue(engine.match_current_line("I think it is a match"))

    def test_exact_match(self):
        engine = RegexEngine("basic")
        self.assertTrue(engine.match_current_line("this is another basic test"))

    def test_wildcard_match(self):
        engine = RegexEngine("a.c")
        self.assertTrue(engine.match_current_line("match a9c here"))

    def test_start_anchor(self):
        engine = RegexEngine("^hello")
        self.assertTrue(engine.match_current_line("hello world"))
        self.assertFalse(engine.match_current_line("say hello"))

    def test_end_anchor(self):
        engine = RegexEngine("world$")
        self.assertTrue(engine.match_current_line("hello world"))
        self.assertFalse(engine.match_current_line("worldwide"))

    def test_both_anchors(self):
        engine = RegexEngine("^hello$")
        self.assertTrue(engine.match_current_line("hello"))
        self.assertFalse(engine.match_current_line("hello world"))
        self.assertFalse(engine.match_current_line(" say hello"))

    def test_anchor_with_wildcard(self):
        engine = RegexEngine("^h.llo$")
        self.assertTrue(engine.match_current_line("hello"))
        self.assertTrue(engine.match_current_line("hallo"))
        self.assertFalse(engine.match_current_line("helloo"))

if __name__ == "__main__":
    unittest.main()
