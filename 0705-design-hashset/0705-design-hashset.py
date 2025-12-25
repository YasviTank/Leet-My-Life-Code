class Node:
    def __init__(self, key, next=None):
        self.key = key
        self.next = next


class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.buckets = [None] * self.size

    def _hash(self, key: int) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        index = self._hash(key)
        cur = self.buckets[index]

        # if bucket is empty
        if not cur:
            self.buckets[index] = Node(key)
            return

        # traverse to check duplicates
        while True:
            if cur.key == key:
                return  # already exists
            if not cur.next:
                break
            cur = cur.next

        # add new node at tail
        cur.next = Node(key)

    def remove(self, key: int) -> None:
        index = self._hash(key)
        cur = self.buckets[index]

        if not cur:
            return

        # remove head
        if cur.key == key:
            self.buckets[index] = cur.next
            return

        # remove from middle or tail
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        index = self._hash(key)
        cur = self.buckets[index]

        while cur:
            if cur.key == key:
                return True
            cur = cur.next

        return False
