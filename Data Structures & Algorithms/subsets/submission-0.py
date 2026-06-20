class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(index, path):
            # This is the base case
            if index == len(nums):
                res.append(path[:])
                return
            # Decision 1 - use current index (add to path)
            path.append(nums[index])
            backtrack(index + 1, path)
            path.pop()
            # Decision 2 - skip current index (do not add to path)
            backtrack(index + 1, path)
        backtrack(0, [])
        return res