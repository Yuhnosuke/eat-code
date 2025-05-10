class ListNode:

    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0

        while curr:
            if index == i:
                return curr.val

            curr = curr.next
            i += 1

        return -1

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        next_node = self.head.next
        prev_node = self.head

        next_node.prev = new_node
        new_node.next = next_node

        prev_node.next = new_node
        new_node.prev = prev_node

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        next_node = self.tail
        prev_node = self.tail.prev

        new_node.next = next_node
        next_node.prev = new_node

        new_node.prev = prev_node
        prev_node.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head.next
        i = 0

        while curr:
            if index == i:
                new_node = ListNode(val)
                next_node = curr
                prev_node = curr.prev

                new_node.next = next_node
                next_node.prev = new_node

                new_node.prev = prev_node
                prev_node.next = new_node

            curr = curr.next
            i += 1

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.next
        i = 0

        while curr and curr != self.tail:
            if index == i:
                next_node = curr.next
                prev_node = curr.prev

                next_node.prev = prev_node
                prev_node.next = next_node

            curr = curr.next
            i += 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
