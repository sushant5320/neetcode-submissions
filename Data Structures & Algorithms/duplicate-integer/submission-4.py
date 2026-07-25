class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # dic={}
        # for i in nums :
        #     if i in dic :
        #         return True
        #     dic[i]=1
        # return False        
                

       nums=sorted(nums)
       for i in range(len(nums)-1) :
        if nums[i]==nums[i+1] :
            return True
       return False     
         