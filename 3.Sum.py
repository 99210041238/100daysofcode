class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return result

# Example usage:
nums1 = [-1, 0, 1, 2, -1, -4]
nums2 = [0, 1, 1]

solution = Solution()
output1 = solution.threeSum(nums1)
output2 = solution.threeSum(nums2)

print(output1)  # Output: [[-1, -1, 2], [-1, 0, 1]]
print(output2)  # Output: []

