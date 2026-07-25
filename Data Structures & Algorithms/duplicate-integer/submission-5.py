class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort() 
        
        # 2. Scan the sorted array
        # We stop at len(nums) - 1 because we check [i] vs [i+1]
        for i in range(len(nums) - 1):
            
            # 3. If neighbor is the same, we found a duplicate
            if nums[i] == nums[i+1]:
                return True
                
        return False