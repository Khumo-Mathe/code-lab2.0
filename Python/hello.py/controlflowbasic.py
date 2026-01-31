import time
from collections import deque

def is_request_allowed(user_id, request_log, max_requests, window_seconds):
    current_time = time.time()

    if user_id not in request_log:
        request_log[user_id] = deque()

    timestamps = request_log[user_id]

    while timestamps and current_time - timestamps[0] > window_seconds:
        timestamps.popleft()

    if len(timestamps) < max_requests:
        timestamps.append(current_time)
        return True

    return False


