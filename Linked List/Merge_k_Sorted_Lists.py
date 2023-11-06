# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # first attempt
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
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

    # second attempt
    def mergeKLists(self, lists):
        """
        use merge sort, where each list
        is the smallest section.
        """
        if len(lists)==0:
            return None

        while len(lists) >1:
            lists = [self.merge(lists[2*i:2*i+2]) for i in range(len(lists)//2+1 if len(lists)%2 else len(lists)//2)]

        return lists[0]


    def merge(self,lst12):
        """
        helper function
        """
        if len(lst12) == 0:
            return None

        if len(lst12) == 1:
            return lst12[0]
        
        lst1,lst2 = lst12

        head = cur = ListNode()
        while lst1 and lst2:
            if lst1.val<lst2.val:
                cur.next = lst1
                lst1, cur = lst1.next, cur.next
            else:
                cur.next = lst2
                lst2, cur = lst2.next, cur.next
        
        cur.next = lst1 if lst1 else lst2

        return head.next
