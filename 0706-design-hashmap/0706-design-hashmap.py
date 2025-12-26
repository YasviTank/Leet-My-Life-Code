class Node:
    def __init__(self, key, val, next=None):
        self.val = val
        self.key = key
        self.next = next


class MyHashMap:

    def __init__(self):
        self.size  = 1000
        self.buckets = [None]*self.size
    
    def _hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        if not self.buckets[index]:
            node = Node(key, value)
            self.buckets[index] = node
            return

        cur = self.buckets[index]
        while cur:
            if cur.key == key:
                cur.val = value
                return
            if not cur.next:
                break
            cur = cur.next
        cur.next = Node(key, value)
        

    def get(self, key: int) -> int:
        index = self._hash(key)
        if not self.buckets[index]:
            return -1
        cur = self.buckets[index]
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1
        

    def remove(self, key: int) -> None:
        index = self._hash(key)
        cur = self.buckets[index]
        if not cur:
            return
        if cur.key == key:
            self.buckets[index] = cur.next
            return
        while cur and cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)