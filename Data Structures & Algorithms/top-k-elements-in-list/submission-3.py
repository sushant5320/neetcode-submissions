class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        for i in range(len(nums)):
            if nums[i] not in cnt:
                cnt[nums[i]] = nums.count(nums[i])
                
        return list(dict(sorted(cnt.items(), key=lambda item: item[1])).keys())[-k:]