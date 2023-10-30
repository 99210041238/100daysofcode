class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert the string to lowercase and remove non-alphanumeric characters
        s = ''.join(filter(str.isalnum, s.lower()))
        
        # Check if the cleaned string is equal to its reverse
        return s == s[::-1]

# Example usage:
s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"
s3 = " "

solution = Solution()
print(solution.isPalindrome(s1))  # Output: True
print(solution.isPalindrome(s2))  # Output: False
print(solution.isPalindrome(s3))  # Output: True
