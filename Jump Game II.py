class Solution:
    def jump(self, nums):
        n = len(nums)
        if n == 1:
            return 0

        # Initialize an array to store the minimum number of jumps to reach each index.
        jumps = [float('inf')] * n
        jumps[0] = 0

        for i in range(1, n):
            for j in range(i):
                if j + nums[j] >= i:
                    jumps[i] = min(jumps[i], jumps[j] + 1)

        return jumps[n - 1]

