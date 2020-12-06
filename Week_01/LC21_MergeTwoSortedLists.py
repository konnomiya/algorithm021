# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    recursion
    T = O(N + M), S = O(N + M), N = len(l1), M = len(l2)
    '''
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
    '''
    iteration
    T = O(N + M), S = O(1)
    '''
    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = dummy = ListNode(-1)
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        if l1:
            head.next = l1
        if l2:
            head.next = l2
        return dummy.next