# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        if headA == headB:
            return headA

        len_a, len_b = 0, 0
        dummy_a, dummy_b = ListNode(0, headA), ListNode(0, headB)

        while headA and headA.next:
            len_a += 1
            headA = headA.next

        while headB and headB.next:
            len_b += 1
            headB = headB.next

        dummy_a = dummy_a.next
        dummy_b = dummy_b.next

        diff = abs(len_a - len_b)

        if len_a > len_b:
            while diff:
                dummy_a = dummy_a.next
                diff -= 1
        elif len_a < len_b:
            while diff:
                dummy_b = dummy_b.next
                diff -= 1

        while dummy_a and dummy_b:
            if dummy_a == dummy_b:
                return dummy_a
            else:
                dummy_a = dummy_a.next
                dummy_b = dummy_b.next

        return None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        a_map = {}

        while headA:
            if headA not in a_map:
                a_map[headA] = 0
            a_map[headA] += 1

            headA = headA.next

        while headB:
            if headB in a_map:
                return headB

            headB = headB.next

        return None
