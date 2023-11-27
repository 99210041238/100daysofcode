from collections import Counter

class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        word_freq = Counter(words)
        result = []

        for i in range(word_len):
            left, right = i, i
            current_window = Counter()

            while right + word_len <= len(s):
                current_word = s[right:right + word_len]
                right += word_len

                if current_word in word_freq:
                    current_window[current_word] += 1

                    while current_window[current_word] > word_freq[current_word]:
                        left_word = s[left:left + word_len]
                        current_window[left_word] -= 1
                        left += word_len

                    if right - left == total_len:
                        result.append(left)

                else:
                    current_window.clear()
                    left = right

            # Reset left and current_window for the next iteration of the outer loop
            left = i
            current_window.clear()

        return result

# Example usage:
solution = Solution()

s1 = "barfoothefoobarman"
words1 = ["foo", "bar"]
print(solution.findSubstring(s1, words1))  # Output: [0, 9]

s2 = "wordgoodgoodgoodbestword"
words2 = ["word", "good", "best", "word"]
print(solution.findSubstring(s2, words2))  # Output: []

s3 = "barfoofoobarthefoobarman"
words3 = ["bar", "foo", "the"]
print(solution.findSubstring(s3, words3))  # Output: [6, 9, 12]
