class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1_copy = nums1[:m]
        nums2_copy = nums2[:n]
        nums1_copy.extend(nums2_copy)
        nums1_copy.sort()
        nums1[:m + n] = nums1_copy
nums1 = [0]
m = 0
nums2 = [1]
n = 1
solution = Solution()
solution.merge(nums1, m, nums2, n)
print(nums1)


