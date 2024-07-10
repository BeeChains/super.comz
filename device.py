class Device:
    def __init__(self, device_id: str):
        self.device_id = device_id
        self.available = True

    def execute(self, task: 'Task'):
        # Simulate task execution
        print(f"Device {self.device_id} is executing task {task.task_id}")
        task.result = f"Result from {self.device_id}"
        return task.result
