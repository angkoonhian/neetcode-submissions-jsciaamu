class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        curr_max_area = 0
        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            curr_max_area = max(area, curr_max_area)
            if heights[right] < heights[left]:
                right -= 1
            else:
                left += 1

        return curr_max_area