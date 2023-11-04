class Solution:
    def maxArea(self, height):
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            h = min(height[left], height[right])
            width = right - left
            area = h * width
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

# Example usage:
height1 = [1,8,6,2,5,4,8,3,7]
solution = Solution()
print(solution.maxArea(height1))  # Output: 49

height2 = [1,1]
print(solution.maxArea(height2))  # Output: 1
