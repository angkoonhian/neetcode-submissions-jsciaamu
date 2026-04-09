class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums = sorted(nums)
        for i in range(len(nums)):
            target = 0 - nums[i]
            if nums[i] == nums[i-1] and i > 0:
                continue
            print(target)
            pairs = self.two_sum_sorted(nums, target, i+1)
            print(pairs)
            if len(pairs) != 0:
                for pair in pairs:
                    res.append([nums[i]] + pair)
        return res


    def two_sum_sorted(self, nums: List[int], target: int, start: int) -> List[int]:

        # Set 2 pointer
        left = start
        right = len(nums)-1
        pairs = []
        while left < right:
            curr_sum = nums[left] + nums[right]
            if curr_sum == target:
                pairs.append([nums[left], nums[right]])
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
            elif curr_sum < target:
                left += 1
            else:
                right -= 1

        return pairs
