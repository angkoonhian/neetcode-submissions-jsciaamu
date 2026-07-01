import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            stone_one = heapq.heappop(heap)
            stone_two = heapq.heappop(heap)
            stone_sum = stone_one - stone_two
            if stone_sum == 0:
                continue
            heapq.heappush(heap, -abs(stone_sum))
        print(heap)
        return -heap[0] if heap else 0
