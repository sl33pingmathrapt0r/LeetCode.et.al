# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        """
        Make 2 partial linked lists:
            ~~Find length of full list, n. Then
            the length of ASC = ceil(n/2).~~ {IGNORE}
        Find middle pointer using race of
        2 pointers: slow points to middle.
        Reverse the link list of second
        part. Merge.
        """

        if not head or not head.next or not head.next.next:
            return

        fast = slow = head
        # slow becomes last node of first part
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        new_h = slow.next
        slow.next = None    # terminate first part

        cur = new_h.next
        new_h.next = None   # terminate second part

        # reverse second part
        while cur:
            temp = cur
            cur = cur.next
            temp.next = new_h
            new_h = temp

        # merge lists
        cur = head; temp_new = new_h
        while cur:
            temp = cur.next
            cur.next = temp_new
            if not temp_new: break
            temp_new = temp_new.next
            cur.next.next = temp
            cur = cur.next.next
