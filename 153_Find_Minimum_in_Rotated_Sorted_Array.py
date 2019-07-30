class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        
        if len(nums) == 1:
            return nums[0]
        
        if nums[right] > nums[0]:
            return nums[0]
        
        while left <= right:
            
            mid = left + (right - left) // 2 # Use // to avoid float indexing
            
            # First check if mid is inflection point
            # Inflection case 1
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            # Inflection case 2
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            
            # If not inflection point
            
            # Min in right part of mid
            if nums[mid] > nums[0]:
                left = mid + 1
            else: # Min in left part of mid
                right = mid - 1
