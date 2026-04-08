class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hashmap approach
        compare = {}
        res = []
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in compare:
                res.append(compare[diff])
                res.append(i)
            else:
                compare[nums[i]] = i

        return res

        #2 pointer approach -- does not work beceause it is not sorted!!!!
        # nums = sorted(nums)
        # start, end = 0, len(nums)-1
        # while start != end:
        #     curr_sum = nums[start] + nums[end]
        #     if curr_sum == target:
        #         return [start, end]
        #     elif curr_sum < target:
        #         start += 1
        #     else:
        #         end -= 1
        # return []