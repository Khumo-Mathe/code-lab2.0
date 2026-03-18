import hashlib


class BloomFilter:
    def __init__(self, size=1000, hash_count=3):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * size

    def _hashes(self, item):
        hashes = []
        for i in range(self.hash_count):
            hash_input = f"{item}-{i}"
            hash_val = int(hashlib.md5(hash_input.encode()).hexdigest(), 16)
            hashes.append(hash_val % self.size)
        return hashes

    def add(self, item):
        for index in self._hashes(item):
            self.bit_array[index] = 1

    def might_contain(self, item):
        for index in self._hashes(item):
            if self.bit_array[index] == 0:
                return False
        return True

