class Solution:
    def removeDuplicates(self, nums):
        if len(nums) <= 2:
            return len(nums)

        slow = 2  # Start from the third element
        count = 2  # Maximum allowed occurrences of each element

        for fast in range(2, len(nums)):
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1

        return slow
