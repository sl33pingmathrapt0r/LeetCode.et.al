# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        2 pointer method: 1 fast and 1 slow pointer;
        if there is a loop, then the 2 pointers must
        eventually meet (LCM)
        """
        if head == None or head.next == None:
            return False

        fast = slow = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False
