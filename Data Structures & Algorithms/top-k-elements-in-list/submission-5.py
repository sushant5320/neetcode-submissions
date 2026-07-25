class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lst = [{i:nums.count(i)} for i in set(nums)]
        dct = dict(sorted({k:v for i in lst for k, v in i.items()}.items(), key=lambda item: item[1]))
        return list(dct.keys())[-k:]