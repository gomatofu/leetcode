class Solution:
    def topKFrequent(self, nums, k):
        counter = Counter(nums)
        heap = []
        
        for num, freq in counter.items():
            heapq.heappush(heap, (-freq, num))
        
        result = []
        for _ in range(k):
            freq, num = heapq.heappop(heap)
            result.append(num)

        return result