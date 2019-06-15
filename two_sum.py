# Problem Number 1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if(complement in mapp):
                return [mapp[complement], i]
            mapp[nums[i]] = i
        
