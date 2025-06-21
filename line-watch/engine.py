class RegexEngine:
    def __init__(self, pattern: str):
        self.pattern = pattern

    def match_current_line(self, line_text: str) -> bool:
        if len(self.pattern) == 0:
            return True

        if self.pattern[0] == '^' or self.pattern[-1] == '$':
            return self.match_with_anchors(line_text)

        line_length = len(line_text)
        pattern_length = len(self.pattern)

        for window_index in range(line_length - pattern_length + 1):
            if self.match_at_specific_position(line_text, window_index):
                return True

        return False

    def match_at_specific_position(self, line_text: str, start_index: int) -> bool:
        for pattern_index in range(len(self.pattern)):
            line_index = start_index + pattern_index
            if line_index >= len(line_text):
                return False

            pattern_character = self.pattern[pattern_index]
            line_character = line_text[line_index]

            if pattern_character != '.' and pattern_character != line_character:
                return False
        return True

    def match_at_pattern(self, pattern: str, line_text: str, start_index: int) -> bool:
        for i in range(len(pattern)):
            if start_index + i >= len(line_text):
                return False
            pc = pattern[i]
            lc = line_text[start_index + i]
            if pc != '.' and pc != lc:
                return False
        return True

    def match_with_anchors(self, line_text: str) -> bool:
        starts_with_caret = self.pattern[0] == '^'
        ends_with_dollar = self.pattern[-1] == '$'

        pattern_chars = []
        for i in range(len(self.pattern)):
            if (starts_with_caret and i == 0) or (ends_with_dollar and i == len(self.pattern) - 1):
                continue
            pattern_chars.append(self.pattern[i])

        stripped_pattern = ""
        for ch in pattern_chars:
            stripped_pattern += ch

        pattern_length = len(stripped_pattern)
        line_length = len(line_text)

        if starts_with_caret and ends_with_dollar:
            if pattern_length != line_length:
                return False
            return self.match_at_pattern(stripped_pattern, line_text, 0)

        elif starts_with_caret:
            if pattern_length > line_length:
                return False
            return self.match_at_pattern(stripped_pattern, line_text, 0)

        elif ends_with_dollar:
            if pattern_length > line_length:
                return False
            start_index = line_length - pattern_length
            return self.match_at_pattern(stripped_pattern, line_text, start_index)

        return False
