from collections import defaultdict
from datetime import datetime


class TaskQueue:
    """
    Simulates a background job processing system.
    Similar to Celery, RabbitMQ workers, or cloud task queues.
    """

    def __init__(self):
        self.pending_tasks = []
        self.completed_tasks = []
        self.failed_tasks = []

    def add_task(self, task_name, payload):
        """
        Add a task to the queue.
        """

        task = {
            "id": len(self.pending_tasks) + 1,
            "task_name": task_name,
            "payload": payload,
            "status": "PENDING",
            "created_at": datetime.now()
        }

        self.pending_tasks.append(task)

        return task

    def process_next_task(self):
        """
        Process the next queued task.
        """

        if not self.pending_tasks:
            return {
                "success": False,
                "message": "No pending tasks"
            }

        task = self.pending_tasks.pop(0)

        try:
            # Simulate processing logic
            result = self.execute_task(task)

            task["status"] = "COMPLETED"
            task["result"] = result
            task["completed_at"] = datetime.now()

            self.completed_tasks.append(task)

            return {
                "success": True,
                "task": task
            }

        except Exception as error:
            task["status"] = "FAILED"
            task["error"] = str(error)

            self.failed_tasks.append(task)

            return {
                "success": False,
                "task": task
            }

    def execute_task(self, task):
        """
        Simulate task execution.
        """

        task_name = task["task_name"]

        if task_name == "send_email":
            return (
                f"Email sent to "
                f"{task['payload']['recipient']}"
            )

        elif task_name == "generate_report":
            return (
                f"Report generated for "
                f"{task['payload']['department']}"
            )

        elif task_name == "resize_image":
            return (
                f"Image resized to "
                f"{task['payload']['resolution']}"
            )

        raise ValueError("Unknown task type")

    def queue_statistics(self):
        """
        Return queue metrics.
        """

        return {
            "pending": len(self.pending_tasks),
            "completed": len(self.completed_tasks),
            "failed": len(self.failed_tasks)
        }


# Example usage
queue = TaskQueue()

queue.add_task(
    task_name="send_email",
    payload={
        "recipient": "khumo@example.com"
    }
)

queue.add_task(
    task_name="generate_report",
    payload={
        "department": "Finance"
    }
)

queue.add_task(
    task_name="resize_image",
    payload={
        "resolution": "1920x1080"
    }
)

processed_1 = queue.process_next_task()
processed_2 = queue.process_next_task()

stats = queue.queue_statistics()