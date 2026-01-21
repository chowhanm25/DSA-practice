class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:
    def __init__(self):
        self.size = 1000  # You can choose a different size if needed
        self.buckets = [None] * self.size

    def _hash(self, key):
        return key % self.size

    def add(self, key):
        index = self._hash(key)
        if not self.contains(key):
            new_node = ListNode(key)
            new_node.next = self.buckets[index]
            self.buckets[index] = new_node

    def remove(self, key):
        index = self._hash(key)
        current = self.buckets[index]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.buckets[index] = current.next
                return
            prev = current
            current = current.next

    def contains(self, key):
        index = self._hash(key)
        current = self.buckets[index]
        while current:
            if current.key == key:
                return True
            current = current.next
        return False

