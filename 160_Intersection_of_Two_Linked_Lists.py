# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        
        if headA is None or headB is None:
            return None
        
        pa = headA
        pb = headB
        
        while pa != pb:
            if pa:
                pa = pa.next
            else:
                pa = headB
            
            if pb:
                pb = pb.next
            else:
                pb = headA
        
        return pa
        """
        Another shorter way:
        
        if headA and headB:
            A, B = headA, headB
            while A!=B:
                A = A.next if A else headB
                B = B.next if B else headA
            return A
        """
