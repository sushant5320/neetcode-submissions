class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]
        for i, j in cnt.items():
            buckets[j].append(i)

        res = []

        for i in range(len(buckets) -1, 0, -1):
            for j in buckets[i]:
                res.append(j)
                if len(res) == k:
                    return res