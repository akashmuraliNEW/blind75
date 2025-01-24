# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
       prev, current = None, head
       while current:
           nxt = current.next
           current.next = prev
           prev = current
           current = nxt
       return prev
