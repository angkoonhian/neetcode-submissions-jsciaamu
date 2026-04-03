class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # what is being repeated?
        # lets try brute force first
        # What is being repeated? it is the 
        prefix = [1] * (len(nums) + 1)
        suffix = [1] * (len(nums) + 1)
        prefix_count, suffix_count = 1, 1
        for i in range(len(nums)):
            prefix_count *= nums[i]
            prefix[i+1] = prefix_count

            suffix_count *= nums[-i-1]
            suffix[-i-1] = suffix_count
        prefix.append(1)
        suffix.append(1)
        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i+2])
        return res
        # return [prefix, suffix]