class Solution:
    def fullJustify(self, words, maxWidth):
        result, line, line_length = [], [], 0
        
        for word in words:
            # Check if the current line can accommodate the word
            if line_length + len(line) + len(word) <= maxWidth:
                line.append(word)
                line_length += len(word)
            else:
                # Distribute spaces evenly in the current line
                spaces = maxWidth - line_length
                if len(line) == 1:
                    result.append(line[0] + ' ' * spaces)
                else:
                    num_gaps = len(line) - 1
                    base_spaces = spaces // num_gaps
                    extra_spaces = spaces % num_gaps
                    line_str = ""
                    for i in range(num_gaps):
                        line_str += line[i] + ' ' * (base_spaces + (i < extra_spaces))
                    line_str += line[-1]
                    result.append(line_str)
                
                # Reset line and line_length for the next line
                line, line_length = [word], len(word)
        
        # Handle the last line
        result.append(' '.join(line).ljust(maxWidth))
        
        return result
