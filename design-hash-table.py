class Pair:

    def __init__(self, key, val):
        self.key = key
        self.val = val


class HashTable:

    def __init__(self, capacity: int):
        self.capacity = capacity  # length of hash table (array)
        self.size = 0  # number of actual data
        self.map = [None] * self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self.hash(key)

        while True:
            # case of create
            if self.map[index] == None:
                self.map[index] = Pair(key, value)
                self.size += 1

                if self.size == self.capacity // 2:
                    self.resize()

                return

            # case of update
            elif self.map[index].key == key:
                self.map[index].val = value
                return

            index += 1
            index = index % self.capacity

    def hash(self, key):
        return key % self.capacity

    def get(self, key: int) -> int:
        index = self.hash(key)

        while self.map[index] != None:
            # case of find
            if self.map[index].key == key:
                return self.map[index].val

            index += 1
            index = index % self.capacity

        return -1

    def remove(self, key: int) -> bool:
        if self.get(key) == -1:
            return False

        index = self.hash(key)

        while True:
            if self.map[index].key == key:
                self.map[index] = None
                self.size -= 1
                return True

            index += 1
            index = index % self.capacity

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        new_map = [None] * self.capacity

        old_map = self.map
        self.map = new_map
        self.size = 0

        for pair in old_map:
            if pair:
                self.insert(pair.key, pair.val)
