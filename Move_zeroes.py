# Problem number 283
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Iterate over the list and swap
        # last zero and last non-zero
        last_zero = 0
        for i in range(0,len(nums)):
            if (nums[i]!=0):
                # Swap
                nums[i], nums[last_zero] = nums[last_zero], nums[i]
                # Increment last_zero pointer
                last_zero += 1
        
