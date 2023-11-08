class Solution:
    def minSubArrayLen(self, target, nums):
        # Initialize pointers and variables
        left, right = 0, 0
        min_length = float('inf')
        current_sum = 0

        # Iterate through the array using the right pointer
        while right < len(nums):
            current_sum += nums[right]
            right += 1

            # Check if the current sum is greater than or equal to the target
            while current_sum >= target:
                # Update the minimum length and move the left pointer
                min_length = min(min_length, right - left)
                current_sum -= nums[left]
                left += 1

        # If no subarray is found, return 0, otherwise return the minimum length
        return min_length if min_length != float('inf') else 0

# Example usage:
target = 7
nums = [2, 3, 1, 2, 4, 3]
solution = Solution()
print(solution.minSubArrayLen(target, nums))  # Output: 2
