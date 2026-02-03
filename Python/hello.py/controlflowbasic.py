import heapq

class TaskScheduler:
    def __init__(self):
        self.queue = []

    def add_task(self, priority, task_name):
        heapq.heappush(self.queue, (-priority, task_name))

    def run_next_task(self):
        if not self.queue:
            return None

        priority, task_name = heapq.heappop(self.queue)
        return task_name



