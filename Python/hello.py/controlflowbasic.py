from collections import OrderedDict


class LRUCache:
    """
    Least Recently Used (LRU) Cache.

    When the cache is full, the least recently
    accessed item is removed first.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        """
        Retrieve a value from cache.

        Returns:
            dict
        """

        if key not in self.cache:
            return {
                "found": False,
                "value": None
            }

        # Move to end because it was recently used
        self.cache.move_to_end(key)

        return {
            "found": True,
            "value": self.cache[key]
        }

    def put(self, key, value):
        """
        Add or update cache entry.
        """

        # Update existing key
        if key in self.cache:
            self.cache.move_to_end(key)

        self.cache[key] = value

        # Remove oldest item if full
        if len(self.cache) > self.capacity:

            evicted_key, evicted_value = (
                self.cache.popitem(last=False)
            )

            return {
                "evicted": {
                    "key": evicted_key,
                    "value": evicted_value
                }
            }

        return {
            "evicted": None
        }

    def current_state(self):
        """
        View cache contents.
        """

        return list(self.cache.items())


# Example usage
cache = LRUCache(capacity=3)

cache.put("user_1", "Khumo")
cache.put("user_2", "Alice")
cache.put("user_3", "Bob")

# Access user_1 (now recently used)
cache.get("user_1")

# Adding another item causes eviction
eviction = cache.put(
    "user_4",
    "Charlie"
)

state = cache.current_state()