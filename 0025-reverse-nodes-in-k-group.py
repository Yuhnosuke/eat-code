# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_group = dummy

        while True:
            kth_node = self.get_kth_node(prev_group, k)
            if not kth_node:
                break
            next_group = kth_node.next

            prev, curr = kth_node.next, prev_group.next
            while curr != next_group:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            next_group_node = prev_group.next
            prev_group.next = kth_node
            prev_group = next_group_node
        return dummy.next

    def get_kth_node(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
