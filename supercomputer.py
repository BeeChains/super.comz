from typing import List
from device import Device
from task import Task
from network_manager import NetworkManager

class SuperComputer:
    def __init__(self):
        self.devices: List[Device] = []
        self.tasks: List[Task] = []
        self.networkManager = NetworkManager()

    def addDevice(self, device: Device):
        self.devices.append(device)
        self.networkManager.connect(device)

    def distributeTask(self, task: Task):
        for device in self.devices:
            if device.available:
                result = self.networkManager.sendTask(device, task)
                if result:
                    print(f"Task {task.task_id} result: {result}")
                    return result
        print(f"No available devices to execute task {task.task_id}")
        return None

    def collectResults(self):
        results = []
        for task in self.tasks:
            result = self.networkManager.receiveResult(task)
            if result:
                results.append(result)
        return results
