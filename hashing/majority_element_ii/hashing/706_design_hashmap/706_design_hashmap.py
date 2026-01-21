class MyHashMap(object):
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key, value):
        index = self._hash(key)
        bucket = self.buckets[index]
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
        bucket.append([key, value])

    def get(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]
        for pair in bucket:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                del bucket[i]
                return

