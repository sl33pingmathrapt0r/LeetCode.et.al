# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # first attempt
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        cache = [lst for lst in lists if lst]

        cur = head = ListNode()
        while cache:
            minim = lambda ls: sorted(ls, key=lambda x: x.val)[0]
            small = cache.index(minim(cache))
            cur.next = cache[small]
            cur, cache[small] = cur.next, cache[small].next
            if not cache[small]:
                cache.pop(small)
        
        return head.next
