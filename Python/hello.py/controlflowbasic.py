import hashlib
import bisect


class ConsistentHashRing:
    def __init__(self, replicas=3):
        self.replicas = replicas
        self.ring = {}
        self.sorted_keys = []

    def _hash(self, key):
        return int(hashlib.md5(key.encode()).hexdigest(), 16)

    def add_node(self, node):
        for i in range(self.replicas):
            virtual_node = f"{node}:{i}"
            hashed_key = self._hash(virtual_node)

            self.ring[hashed_key] = node
            self.sorted_keys.append(hashed_key)

        self.sorted_keys.sort()

    def remove_node(self, node):
        for i in range(self.replicas):
            virtual_node = f"{node}:{i}"
            hashed_key = self._hash(virtual_node)

            del self.ring[hashed_key]
            self.sorted_keys.remove(hashed_key)

    def get_node(self, key):
        if not self.ring:
            return None

        hashed_key = self._hash(key)

        index = bisect.bisect(self.sorted_keys, hashed_key)

        if index == len(self.sorted_keys):
            index = 0

        return self.ring[self.sorted_keys[index]]


