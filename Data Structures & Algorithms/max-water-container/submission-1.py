class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        res = 0
        while left < right:
            curr_area = min(heights[right], heights[left]) * (right - left)
            res = max(curr_area, res)
            if heights[right] < heights[left]:
                right -= 1
            else:
                left += 1
        return res

            