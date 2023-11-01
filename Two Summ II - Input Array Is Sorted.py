class Solution:
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]  # 1-indexed array

            if current_sum < target:
                left += 1
            else:
                right -= 1

        # No solution found, but the problem statement guarantees a solution exists.
        return []

# Example usage
numbers = [2, 7, 11, 15]
target = 9
solution = Solution()
result = solution.twoSum(numbers, target)
print(result)  # Output: [1, 2]
