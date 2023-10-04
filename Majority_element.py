class Solution:
    def majorityElement(self, nums):
        majority = None
        count = 0
        for num in nums:
            if count == 0:
                majority = num
                count = 1
            elif num == majority:
                count += 1
            else:
                count -= 1
        count = 0
        for num in nums:
            if num == majority:
                count += 1
        if count > len(nums) // 2:
            return majority
        else:
            return None  

# Example usage:
nums = [3, 3, 4, 2, 4, 4, 2, 4, 4]
solution = Solution()
result = solution.majorityElement(nums)
print("Majority Element:", result)
