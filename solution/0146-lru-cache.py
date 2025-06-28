class ListNode:

    def __init__(self, key, val):
        self.key = key
        self.val = val

        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # to get node with O(1) operation
        # key: key, value: ListNode
        self.cache = {}

        # use doubly linked list to represent the order of least recently used

        # dummy node for Least Recently Used
        self.head = ListNode(-1, -1)
        # dummy node for Most Recently Used
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev, next = node.prev, node.next

        prev.next, next.prev = next, prev

    def _insert_at_tail(self, node):
        prev, next = self.tail.prev, self.tail

        prev.next, node.prev = node, prev
        node.next, next.prev = next, node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # in order to make the node the most recent used,
            # firstly, remove from linked list
            self._remove(node)
            # then insert at tail in linked list
            self._insert_at_tail(node)
            return node.val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # to make the node the most recent used
            self._remove(self.cache[key])

        # create ListNode
        node = ListNode(key, value)
        # store in cache
        self.cache[key] = node
        # make the node the most recent used
        self._insert_at_tail(node)

        if len(self.cache) > self.capacity:
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
