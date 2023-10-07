class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0 
        unique_count = 1 
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[unique_count] = nums[i]
                unique_count += 1
        return unique_count
nums = [1, 1, 2]
solution = Solution()
k = solution.removeDuplicates(nums)
expectedNums = [1, 2]
assert k == len(expectedNums)
for i in range(k):
    assert nums[i] == expectedNums[i]
print(nums[:k] + ['_'] * (len(nums) - k))
