class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the input string into words using spaces as the delimiter.
        words = s.split()

        # Reverse the order of the words.
        reversed_words = words[::-1]

        # Join the reversed words with a single space.
        reversed_s = ' '.join(reversed_words)

        return reversed_s

