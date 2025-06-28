from typing import List


class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        i = 0
        curr = self.head.next

        while curr:
            if index == i:
                return curr.val

            i += 1
            curr = curr.next

        return -1

    def insertHead(self, val: int) -> None:
        node = ListNode(val)

        node.next = self.head.next
        self.head.next = node

        if not node.next:
            self.tail = node

    def insertTail(self, val: int) -> None:
        node = ListNode(val)
        self.tail.next = node
        self.tail = node

    def remove(self, index: int) -> bool:
        prev = self.head
        curr = self.head.next

        i = 0

        while curr:
            if i == index:
                prev.next = curr.next
                if not prev.next:
                    self.tail = prev
                return True

            i += 1
            prev = prev.next
            curr = curr.next

        return False

    def getValues(self) -> List[int]:
        curr = self.head.next
        res = []

        while curr:
            res.append(curr.val)
            curr = curr.next

        return res
