import hashlib


class HyperLogLog:
    def __init__(self, num_buckets=16):
        self.num_buckets = num_buckets
        self.buckets = [0] * num_buckets

    def _hash(self, item):
        return int(hashlib.md5(item.encode()).hexdigest(), 16)

    def _leading_zeros(self, binary_str):
        count = 0
        for bit in binary_str:
            if bit == '0':
                count += 1
            else:
                break
        return count

    def add(self, item):
        hashed = self._hash(item)

        bucket_index = hashed % self.num_buckets

        binary = bin(hashed)[2:]

        zeros = self._leading_zeros(binary)

        self.buckets[bucket_index] = max(self.buckets[bucket_index], zeros)

    def estimate(self):
        total = sum([2 ** (-bucket) for bucket in self.buckets])
        return int(self.num_buckets ** 2 / total)