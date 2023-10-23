class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        # Sort the input list of strings
        strs.sort()

        # Take the first and last strings after sorting
        first_str = strs[0]
        last_str = strs[-1]

        # Find the common prefix between the first and last strings
        prefix = []
        for i in range(min(len(first_str), len(last_str))):
            if first_str[i] == last_str[i]:
                prefix.append(first_str[i])
            else:
                break

        return "".join(prefix)

# Example usage:
strs1 = ["flower", "flow", "flight"]
strs2 = ["dog", "racecar", "car"]
solution = Solution()

print(solution.longestCommonPrefix(strs1))  # Output: "fl"
print(solution.longestCommonPrefix(strs2))  # Output: ""

