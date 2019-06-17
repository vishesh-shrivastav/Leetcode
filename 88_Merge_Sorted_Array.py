class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        """
        Method 1 - merge both arrays and then sort
        
        nums1[:] = sorted(nums[:m] + nums2)
        """
        
        """
        Method 2 - Two pointer approach
        """
        n1copy = nums1[:m]
        nums1[:] = []
        p1, p2 = 0, 0
        
        while (p1 < m and p2 < n):
            if n1copy[p1] < nums2[p2]:
                nums1.append(n1copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1
        
        if p1 < m:
            nums1[p1 + p2:] = n1copy[p1:]
        if p2 < n:
            nums1[p1 + p2:] = nums2[p2:]
