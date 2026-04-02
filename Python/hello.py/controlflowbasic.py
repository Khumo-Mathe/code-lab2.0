import time
import uuid


class DistributedLock:
    def __init__(self):
        self.locks = {}

    def acquire_lock(self, resource, ttl=5):
        current_time = time.time()
        lock_id = str(uuid.uuid4())

        if resource not in self.locks:
            self.locks[resource] = (lock_id, current_time + ttl)
            return lock_id

        existing_lock_id, expiry = self.locks[resource]

        if current_time > expiry:
            self.locks[resource] = (lock_id, current_time + ttl)
            return lock_id

        return None

    def release_lock(self, resource, lock_id):
        if resource in self.locks:
            existing_lock_id, _ = self.locks[resource]

            if existing_lock_id == lock_id:
                del self.locks[resource]
                return True

        return False