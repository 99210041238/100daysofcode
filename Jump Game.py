class Solution:
    def canJump(self, nums):
        if not nums:
            return False

        n = len(nums)
        farthest = 0

        for i in range(n):
            if i > farthest:
                return False  # Cannot reach the end
            farthest = max(farthest, i + nums[i])

        return farthest >= n - 1  # Check if the farthest position can reach the last inde
        