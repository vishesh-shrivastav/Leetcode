class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        count = 0 # Count of non-zero elements 
        # Traverse the array. If element  
        # encountered is non-zero, then 
        # replace the element at index 
        # 'count' with this element 
        for i in range(len(nums)): 
            if nums[i] != 0: 

                # here count is incremented 
                nums[count] = nums[i] 
                count+=1

        # Now all non-zero elements have been 
        # shifted to front and 'count' is set 
        # as index of first 0. Make all  
        # elements 0 from count to end. 
        while count < len(nums): 
            nums[count] = 0
            count += 1
