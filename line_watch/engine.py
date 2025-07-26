class RegexEngine:
    def __init__(self, pattern: str):
        self.pattern = pattern

    def match_current_line(self, line_text: str) -> bool:
        if not self.pattern:
            return True

        if self._has_anchors():
            return self._match_with_anchors(line_text)

        for start_index in range(len(line_text)):
            if self._match_at(line_text, self.pattern, start_index):
                return True
        return False

    def _match_at(self, text: str, pattern: str, start: int) -> bool:
        t_idx = start
        p_idx = 0

        while p_idx < len(pattern):
            if t_idx > len(text):
                return False

            if p_idx + 1 < len(pattern) and pattern[p_idx + 1] in '*+?':
                quant = pattern[p_idx + 1]
                unit, next_p_idx = self._get_unit(pattern, p_idx)
                if quant == '*':
                    t_idx = self._match_quant_star(unit, text, t_idx)
                elif quant == '+':
                    new_idx = self._match_quant_plus(unit, text, t_idx)
                    if new_idx == -1:
                        return False
                    t_idx = new_idx
                elif quant == '?':
                    t_idx = self._match_quant_question(unit, text, t_idx)
                p_idx = next_p_idx + 1
            else:
                unit, next_p_idx = self._get_unit(pattern, p_idx)
                if t_idx >= len(text) or not self._char_matches_unit(unit, text[t_idx]):
                    return False
                t_idx += 1
                p_idx = next_p_idx + 1

        return t_idx <= len(text)

    def _match_star(self, char: str, text: str, t_idx: int) -> int:
        while t_idx < len(text) and (char == '.' or text[t_idx] == char):
            t_idx += 1
        return t_idx

    def _match_plus(self, char: str, text: str, t_idx: int) -> int:
        if t_idx >= len(text) or (char != '.' and text[t_idx] != char):
            return -1
        t_idx += 1
        while t_idx < len(text) and (char == '.' or text[t_idx] == char):
            t_idx += 1
        return t_idx

    def _match_question(self, char: str, text: str, t_idx: int) -> int:
        if t_idx < len(text) and (char == '.' or text[t_idx] == char):
            return t_idx + 1
        return t_idx

    def _has_anchors(self) -> bool:
        return self.pattern.startswith('^') or self.pattern.endswith('$')

    def _match_with_anchors(self, text: str) -> bool:
        starts_with_caret = self.pattern.startswith('^')
        ends_with_dollar = self.pattern.endswith('$')

        core_start = 1 if starts_with_caret else 0
        core_end = -1 if ends_with_dollar else len(self.pattern)
        core_pattern = self.pattern[core_start:core_end]

        if starts_with_caret and ends_with_dollar:
            return self._match_at(text, core_pattern, 0) and len(core_pattern) == len(text)

        if starts_with_caret:
            return self._match_at(text, core_pattern, 0)

        if ends_with_dollar:
            start = len(text) - len(core_pattern)
            return self._match_at(text, core_pattern, start) if start >= 0 else False

        return False

def _get_unit(self, pattern: str, idx: int) -> tuple:
    if pattern[idx] == '[':
        closing = pattern.find(']', idx)
        if closing == -1:
            raise ValueError("Unclosed character class")
        return pattern[idx:closing + 1], closing
    return pattern[idx], idx

def _char_matches_unit(self, unit: str, char: str) -> bool:
    if unit.startswith('[') and unit.endswith(']'):
        return char in unit[1:-1]
    return unit == '.' or unit == char

def _match_quant_star(self, unit: str, text: str, t_idx: int) -> int:
    while t_idx < len(text) and self._char_matches_unit(unit, text[t_idx]):
        t_idx += 1
    return t_idx

def _match_quant_plus(self, unit: str, text: str, t_idx: int) -> int:
    if t_idx >= len(text) or not self._char_matches_unit(unit, text[t_idx]):
        return -1
    t_idx += 1
    while t_idx < len(text) and self._char_matches_unit(unit, text[t_idx]):
        t_idx += 1
    return t_idx

def _match_quant_question(self, unit: str, text: str, t_idx: int) -> int:
    if t_idx < len(text) and self._char_matches_unit(unit, text[t_idx]):
        return t_idx + 1
    return t_idx
