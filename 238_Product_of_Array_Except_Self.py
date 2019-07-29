class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [0] * len(nums)
        res[0] = 1
        
        for i in range(1,len(nums)):
            res[i] = res[i-1] * nums[i-1]
            
        right = 1
        
        #for i in reversed(range(len(nums))):
        for i in range(len(nums)-1, -1, -1):  #faster than reversed()
            res[i] = right * res[i]
            right *= nums[i]
        
        return res
