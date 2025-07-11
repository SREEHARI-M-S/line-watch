import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from line_watch.engine import RegexEngine

class TestRegexEngine(unittest.TestCase):

    def test_should_match_substring(self):
        engine = RegexEngine("basic")
        self.assertTrue(engine.match_current_line("this is a basic test"), "Expected to match 'basic' substring")

    def test_should_not_match_unrelated_substring(self):
        engine = RegexEngine("no-basic")
        self.assertFalse(engine.match_current_line("this is not a basic test"), "Expected not to match 'no-basic'")

    def test_should_match_any_line_for_empty_pattern(self):
        engine = RegexEngine("")
        self.assertTrue(engine.match_current_line("any content should match"), "Empty pattern should match anything")

    def test_should_match_exact_pattern(self):
        engine = RegexEngine("basic")
        self.assertTrue(engine.match_current_line("this is another basic test"))

    def test_should_match_start_anchor(self):
        engine = RegexEngine("^hello")
        self.assertTrue(engine.match_current_line("hello world"))
        self.assertFalse(engine.match_current_line("say hello world"))

    def test_should_match_end_anchor(self):
        engine = RegexEngine("world$")
        self.assertTrue(engine.match_current_line("hello world"))
        self.assertFalse(engine.match_current_line("worldwide"))

    def test_should_match_exact_anchors(self):
        engine = RegexEngine("^hello$")
        self.assertTrue(engine.match_current_line("hello"))
        self.assertFalse(engine.match_current_line("hello world"))
        self.assertFalse(engine.match_current_line(" say hello"))

    def test_should_match_anchor_with_dot(self):
        engine = RegexEngine("^h.llo$")
        self.assertTrue(engine.match_current_line("hello"))
        self.assertTrue(engine.match_current_line("hallo"))
        self.assertFalse(engine.match_current_line("helloo"))

    def test_pattern_longer_than_text(self):
        engine = RegexEngine("superlongpattern")
        self.assertFalse(engine.match_current_line("short"))

    def test_should_match_with_dot_wildcard(self):
        engine = RegexEngine("a.c")
        self.assertTrue(engine.match_current_line("look at a9c happening here"))
        self.assertTrue(engine.match_current_line("no match for abcde"))

    def test_wildcard_at_end(self):
        engine = RegexEngine("en.")
        self.assertTrue(engine.match_current_line("open file"))
        self.assertTrue(engine.match_current_line("openness"))

    def test_star_quantifier(self):
        engine = RegexEngine("ab*c")
        self.assertTrue(engine.match_current_line("abc"))
        self.assertTrue(engine.match_current_line("ac"))
        self.assertTrue(engine.match_current_line("abbbbbc"))
        self.assertFalse(engine.match_current_line("ab"))

    def test_plus_quantifier(self):
        engine = RegexEngine("ab+c")
        self.assertTrue(engine.match_current_line("abc"))
        self.assertTrue(engine.match_current_line("abbbbbc"))
        self.assertFalse(engine.match_current_line("ac"))

    def test_question_quantifier(self):
        engine = RegexEngine("ab?c")
        self.assertTrue(engine.match_current_line("abc"))
        self.assertTrue(engine.match_current_line("ac"))
        self.assertFalse(engine.match_current_line("abbc"))

if __name__ == "__main__":
    unittest.main()
