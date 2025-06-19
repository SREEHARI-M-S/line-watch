class RegexEngine:
    def __init__(self, pattern: str):
        self.pattern = pattern
    
    def match_current_line(self, line_text: str) -> bool:
        pattern_length = len(self.pattern)
        line_length = len(line_text)

        if pattern_length == 0:
            return True
        
        for window_current_index in range(line_length - pattern_length + 1):
            if self.match_at_position(line_text, window_current_index):
                return True

        return False
    
    def match_at_specific_position(self, line_text: str, start_index: int) -> bool:
        for pattern_index in range(len(self.pattern)):
            line_index = start_index + pattern_index
            line_character = line_text[line_index]
            pattern_character = self.pattern[pattern_index]

            if pattern_character != '.' and pattern_character != line_character:
                return False
        return True
