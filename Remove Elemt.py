class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)  
            else:
                i += 1 

# Example usage:
solution = Solution()
nums = [1, 2, 3, 4, 5, 5, 6]
val = 5
solution.removeElement(nums, val)
print(nums)  
