# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next

            curr.next = prev

            prev = curr
            curr = next_node

        return prev


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if not head:
            return None

        # node as head to return finally
        new_head = head

        if head.next:
            # traverse recursively until last node
            # and get new node
            new_head = self.reverseList(head.next)
            # reverse node
            head.next.next = head
        # cut the link of current node
        head.next = None

        return new_head
