# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not list or len(lists) == 0:
            return None

        while len(lists) > 1:

            merged = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if i + 1 < len(lists) else None

                merged.append(self.merge_list(list1, list2))

            lists = merged

        return lists[0]

    def merge_list(self, list1, list2):
        head = ListNode(-1)
        curr = head

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1

                list1 = list1.next
            else:
                curr.next = list2

                list2 = list2.next
            curr = curr.next

        if list1:
            curr.next = list1
        if list2:
            curr.next = list2

        return head.next
