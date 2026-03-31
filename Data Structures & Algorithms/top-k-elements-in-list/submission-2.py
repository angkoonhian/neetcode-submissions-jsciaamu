class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {}
        res = []
        for num in nums:
            if num not in store:
                store[num] = 1
            else:
                store[num] += 1

        for key, val in store.items():
            res.append([val, key])
        res.sort(reverse=True)
        return list(map(lambda n: n[1], res[:k]))