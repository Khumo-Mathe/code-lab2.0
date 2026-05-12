from collections import deque


class RateLimiter:
    """
    Simple API Rate Limiter using Sliding Window logic.

    Restricts how many requests a user can make
    within a time window.
    """

    def __init__(self, max_requests, window_seconds):
        self.max_requests = max_requests
        self.window_seconds = window_seconds

        # Store request timestamps per user
        self.user_requests = {}

    def allow_request(self, user_id, current_time):
        """
        Check whether a request should be allowed.

        Args:
            user_id (str): Unique user identifier
            current_time (int): Current timestamp in seconds

        Returns:
            bool: True if allowed, False otherwise
        """

        if user_id not in self.user_requests:
            self.user_requests[user_id] = deque()

        requests = self.user_requests[user_id]

        # Remove expired requests outside the window
        while requests and (
            current_time - requests[0]
        ) >= self.window_seconds:
            requests.popleft()

        # Block if limit reached
        if len(requests) >= self.max_requests:
            return False

        # Store current request timestamp
        requests.append(current_time)

        return True


# Example usage
limiter = RateLimiter(
    max_requests=3,
    window_seconds=10
)

results = [
    limiter.allow_request("khumo", 1),
    limiter.allow_request("khumo", 2),
    limiter.allow_request("khumo", 3),
    limiter.allow_request("khumo", 4),  # Blocked
    limiter.allow_request("khumo", 12)  # Allowed again
]