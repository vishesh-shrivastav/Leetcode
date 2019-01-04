# Problem number 88
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # Start filling nums from the end
        a, b = m-1, n-1
        while a>=0 and b>=0:
            if nums1[a] > nums2[b]:
                nums1[a+b+1] = nums1[a]
                a -= 1
            else:
                nums1[a+b+1] = nums2[b]
                b -= 1
        # Boundary case for inputs like ([0],0,[1],1)
        if b>=0:
            nums1[:b+1] = nums2[:b+1]
