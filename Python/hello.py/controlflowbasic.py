from collections import defaultdict
from datetime import datetime


class APICache:
    """
    Simple in-memory caching system.

    Reduces repeated expensive API/database calls.
    """

    def __init__(self):
        self.cache = {}
        self.cache_hits = 0
        self.cache_misses = 0
        self.request_frequency = defaultdict(int)

    def set(
        self,
        key,
        value,
        ttl_seconds
    ):
        """
        Store data in cache.
        """

        expiration_time = (
            datetime.now().timestamp()
            + ttl_seconds
        )

        self.cache[key] = {
            "value": value,
            "expires_at": expiration_time
        }

    def get(self, key):
        """
        Retrieve cached data if valid.
        """

        self.request_frequency[key] += 1

        if key not in self.cache:
            self.cache_misses += 1

            return {
                "found": False,
                "value": None
            }

        cached_item = self.cache[key]

        current_time = datetime.now().timestamp()

        # Remove expired cache entries
        if current_time > cached_item["expires_at"]:

            del self.cache[key]

            self.cache_misses += 1

            return {
                "found": False,
                "value": None
            }

        self.cache_hits += 1

        return {
            "found": True,
            "value": cached_item["value"]
        }

    def delete(self, key):
        """
        Remove cache entry.
        """

        if key in self.cache:
            del self.cache[key]

            return {
                "success": True
            }

        return {
            "success": False,
            "message": "Key not found"
        }

    def statistics(self):
        """
        Return cache performance metrics.
        """

        total_requests = (
            self.cache_hits
            + self.cache_misses
        )

        hit_rate = 0

        if total_requests > 0:
            hit_rate = round(
                (
                    self.cache_hits
                    / total_requests
                ) * 100,
                2
            )

        return {
            "cache_hits": self.cache_hits,
            "cache_misses": self.cache_misses,
            "hit_rate_percent": hit_rate,
            "stored_keys": len(self.cache)
        }


# Example usage
cache = APICache()

cache.set(
    key="user_100_profile",
    value={
        "name": "Khumo",
        "role": "Developer"
    },
    ttl_seconds=300
)

profile = cache.get(
    "user_100_profile"
)

missing_data = cache.get(
    "unknown_key"
)

stats = cache.statistics()