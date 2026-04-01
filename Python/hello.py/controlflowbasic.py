import time


class TokenBucket:
    def __init__(self, capacity, refill_rate):
        self.capacity = capacity          # max tokens
        self.tokens = capacity            # current tokens
        self.refill_rate = refill_rate    # tokens per second
        self.last_refill = time.time()

    def _refill(self):
        current_time = time.time()
        elapsed = current_time - self.last_refill

        new_tokens = elapsed * self.refill_rate
        self.tokens = min(self.capacity, self.tokens + new_tokens)

        self.last_refill = current_time

    def allow_request(self):
        self._refill()

        if self.tokens >= 1:
            self.tokens -= 1
            return True

        return False