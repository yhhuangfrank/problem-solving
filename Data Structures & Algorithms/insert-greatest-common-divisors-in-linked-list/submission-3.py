# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def find_gcd(cur, nxt):
            v1, v2 = min(cur.val, nxt.val), max(cur.val, nxt.val)
            if v2 % v1 == 0:
                return v1
            gcd = 1
            i = 2
            while i * i <= v1:
                if v1 % i == 0:
                    div = v1 // i
                    if v2 % i == 0:
                        gcd = max(gcd, i)
                    if v2 % div == 0:
                        gcd = max(gcd, div)
                i += 1
            return gcd

        dummy = ListNode(0, head)
        dummy.next = head
        cur = head
        while cur.next:
            nxt = cur.next
            gcd = find_gcd(cur, nxt)
            gcd_node = ListNode(gcd)
            cur.next = gcd_node
            gcd_node.next = nxt
            cur = nxt
        return dummy.next