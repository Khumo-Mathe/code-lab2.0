from datetime import datetime
import heapq


class Scheduler:
    """
    Priority-based task scheduler.

    Similar to operating system schedulers,
    job schedulers, and cloud orchestration systems.
    """

    def __init__(self):
        self.task_queue = []
        self.completed_tasks = []

    def schedule_task(
        self,
        task_name,
        priority,
        execution_time
    ):
        """
        Add a task to the scheduler.

        Lower priority number = higher priority.
        """

        task = {
            "task_name": task_name,
            "priority": priority,
            "execution_time": execution_time,
            "created_at": datetime.now()
        }

        heapq.heappush(
            self.task_queue,
            (
                priority,
                datetime.now().timestamp(),
                task
            )
        )

        return task

    def run_next_task(self):
        """
        Execute the highest-priority task.
        """

        if not self.task_queue:
            return {
                "success": False,
                "message": "No pending tasks"
            }

        _, _, task = heapq.heappop(
            self.task_queue
        )

        task["status"] = "COMPLETED"
        task["completed_at"] = datetime.now()

        self.completed_tasks.append(task)

        return {
            "success": True,
            "task": task
        }

    def pending_tasks(self):
        """
        View pending tasks.
        """

        return [
            item[2]
            for item in self.task_queue
        ]

    def statistics(self):
        """
        Scheduler metrics.
        """

        return {
            "pending_tasks": len(
                self.task_queue
            ),
            "completed_tasks": len(
                self.completed_tasks
            )
        }


# Example usage
scheduler = Scheduler()

scheduler.schedule_task(
    task_name="Backup Database",
    priority=1,
    execution_time=300
)

scheduler.schedule_task(
    task_name="Generate Reports",
    priority=3,
    execution_time=120
)

scheduler.schedule_task(
    task_name="Send Emails",
    priority=2,
    execution_time=60
)

next_task = scheduler.run_next_task()

stats = scheduler.statistics()