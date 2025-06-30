class RegexEngine:
    def __init__(self, pattern: str):
        self.pattern = pattern

    def match_current_line(self, line_text: str) -> bool:
        if not self.pattern:
            return True

        if self.pattern.startswith('^') or self.pattern.endswith('$'):
            return self._match_with_anchors(line_text)

        for i in range(len(line_text) - len(self.pattern) + 1):
            if self._match_at_position(line_text, self.pattern, i):
                return True

        return False

    def _match_at_position(self, line_text: str, pattern: str, start_index: int) -> bool:
        for i in range(len(pattern)):
            if start_index + i >= len(line_text):
                return False
            p_char = pattern[i]
            l_char = line_text[start_index + i]
            if p_char != '.' and p_char != l_char:
                return False
        return True

    def _match_with_anchors(self, line_text: str) -> bool:
        starts_with_caret = self.pattern.startswith('^')
        ends_with_dollar = self.pattern.endswith('$')

        start_idx = 1 if starts_with_caret else 0
        end_idx = -1 if ends_with_dollar else len(self.pattern)
        core_pattern = self.pattern[start_idx:end_idx]

        if starts_with_caret and ends_with_dollar:
            return len(line_text) == len(core_pattern) and self._match_at_position(line_text, core_pattern, 0)

        if starts_with_caret:
            return len(line_text) >= len(core_pattern) and self._match_at_position(line_text, core_pattern, 0)

        if ends_with_dollar:
            start = len(line_text) - len(core_pattern)
            return start >= 0 and self._match_at_position(line_text, core_pattern, start)

        return False
