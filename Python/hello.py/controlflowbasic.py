
import time
import random


def retry_with_backoff(operation, max_retries=5, base_delay=1.0):
    attempts = 0

    while attempts < max_retries:
        try:
            return operation()

        except Exception as e:
            delay = base_delay * (2 ** attempts)
            jitter = random.uniform(0, delay)

            time.sleep(jitter)

            attempts += 1

    return None