# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Using 2 pointers, one points
        ahead by n nodes. E.g.
        {START} -> 0-> 1 -> 2 -> 3 -> 4, | n=2
        => when ahead.next=None,
        behind is before the node to
        be removed.
        """
        if not head:
            return head

        behind = ahead = ListNode()
        behind.next = head
        for _ in range(n):
            ahead = ahead.next
        
        flag = False
        while ahead.next:
            flag = True
            behind, ahead = behind.next, ahead.next
        
        if flag:
            behind.next = behind.next.next
            return head
        
        return head.next
