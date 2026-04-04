class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        compare = defaultdict(int)
        res = 0
        for num in nums:
            if not compare[num]:
                length = compare[num-1] + compare[num+1] + 1
                # set current num consec length
                compare[num] = length
                # need to update lower bound with new consec length
                compare[num - compare[num-1]] = length
                # need to update uppper bound with new consec length
                compare[num + compare[num+1]] = length
                res = max(res, length)
        return res