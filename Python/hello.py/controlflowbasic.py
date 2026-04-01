import time


class CircuitBreaker:
    def __init__(self, failure_threshold=3, recovery_time=5):
        self.failure_threshold = failure_threshold
        self.recovery_time = recovery_time

        self.failure_count = 0
        self.state = "CLOSED"
        self.last_failure_time = None

    def call(self, operation):
        if self.state == "OPEN":
            if time.time() - self.last_failure_time > self.recovery_time:
                self.state = "HALF-OPEN"
            else:
                return None

        try:
            result = operation()

            if self.state == "HALF-OPEN":
                self.state = "CLOSED"
                self.failure_count = 0

            return result

        except Exception:
            self.failure_count += 1
            self.last_failure_time = time.time()

            if self.failure_count >= self.failure_threshold:
                self.state = "OPEN"

            return None