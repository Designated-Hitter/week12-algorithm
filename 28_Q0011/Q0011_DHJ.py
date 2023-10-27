class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum = 0
        left = 0
        right = len(height) - 1

        while left < right:
            wall = min(height[left], height[right])
            width = right - left
            maximum = max(maximum, wall * width)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maximum