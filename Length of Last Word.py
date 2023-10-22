class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Remove trailing and leading spaces
        s = s.strip()
        if not s:
            return 0

        # Split the string by spaces and return the length of the last word
        words = s.split()
        return len(words[-1])

# Example usage:
solution = Solution()
input1 = "Hello World"
output1 = solution.lengthOfLastWord(input1)
print(output1)  # Output: 5

input2 = "   fly me   to   the moon  "
output2 = solution.lengthOfLastWord(input2)
print(output2)  # Output: 4

input3 = "luffy is still joyboy"
output3 = solution.lengthOfLastWord(input3)
print(output3)  # Output: 6
