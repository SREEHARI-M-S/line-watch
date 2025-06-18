class RegexEngine:
    def __init__(self, pattern: str):
        self.pattern = pattern
    
    def match_current_line(self, line_text: str) -> bool:
        pattern_length = len(self.pattern)
        line_length = len(line_text)

        if pattern_length == 0:
            return True
        
        for window_current_index in range(line_length - pattern_length + 1):
            is_pattern_matched = True
            for pattern_current_index in range(pattern_length):
                if current_line[window_current_index + pattern_current_index] != self.pattern[pattern_current_index]:
                    is_pattern_matched = False
                    break
            if is_pattern_matched:
                return True
        return False