# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def find_gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        dummy = ListNode(0, head)
        dummy.next = head
        cur = head
        while cur.next:
            nxt = cur.next
            gcd = find_gcd(cur.val, nxt.val)
            gcd_node = ListNode(gcd)
            cur.next = gcd_node
            gcd_node.next = nxt
            cur = nxt
        return dummy.next