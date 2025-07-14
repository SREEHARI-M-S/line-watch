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
                if quant == '*':
                    t_idx = self._match_star(pattern[p_idx], text, t_idx)
                elif quant == '+':
                    new_idx = self._match_plus(pattern[p_idx], text, t_idx)
                    if new_idx == -1:
                        return False
                    t_idx = new_idx
                elif quant == '?':
                    t_idx = self._match_question(pattern[p_idx], text, t_idx)
                p_idx += 2
            else:
                if t_idx >= len(text) or (pattern[p_idx] != '.' and pattern[p_idx] != text[t_idx]):
                    return False
                p_idx += 1
                t_idx += 1

        return True 


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

