class RegexEngine:
    def __init__(self, pattern: str):
        self.pattern = pattern

    def match_current_line(self, line_text: str) -> bool:
        if not self.pattern:
            return True

        if self._has_anchors():
            return self._match_with_anchors(line_text)

        # Try matching at every possible position in the text
        for start_index in range(len(line_text) - len(self.pattern) + 1):
            if self._match_at(line_text, self.pattern, start_index):
                return True
        return False

    def _match_at(self, text: str, pattern: str, start: int) -> bool:
        if start + len(pattern) > len(text):
            return False

        for i, p_char in enumerate(pattern):
            l_char = text[start + i]
            if p_char != '.' and p_char != l_char:
                return False
        return True

    def _has_anchors(self) -> bool:
        return self.pattern.startswith('^') or self.pattern.endswith('$')

    def _match_with_anchors(self, text: str) -> bool:
        starts_with_caret = self.pattern.startswith('^')
        ends_with_dollar = self.pattern.endswith('$')

        core_start = 1 if starts_with_caret else 0
        core_end = -1 if ends_with_dollar else len(self.pattern)
        core_pattern = self.pattern[core_start:core_end]

        if starts_with_caret and ends_with_dollar:
            return len(text) == len(core_pattern) and self._match_at(text, core_pattern, 0)

        if starts_with_caret:
            return self._match_at(text, core_pattern, 0)

        if ends_with_dollar:
            start = len(text) - len(core_pattern)
            return self._match_at(text, core_pattern, start) if start >= 0 else False

        return False
