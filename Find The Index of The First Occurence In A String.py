class Solution:
    def strStr(self, haystack, needle):
        if not needle:
            return 0  # Empty needle, return 0.

        if len(needle) > len(haystack):
            return -1  # Needle is longer than haystack, impossible to find.

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1  # Needle not found in haystack.

