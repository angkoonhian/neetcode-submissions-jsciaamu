class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # what is being reepeated?
        # lets try brute force first
        res = []
        for i in range(len(nums)):
            curr = 1
            for j in range(len(nums)):
                if j != i:
                    curr  *= nums[j]
            res.append(curr)
        return res