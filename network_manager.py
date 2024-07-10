from typing import Dict
from device import Device
from task import Task

class NetworkManager:
    def __init__(self):
        self.network_map: Dict[str, Device] = {}

    def connect(self, device: Device):
        self.network_map[device.device_id] = device
        print(f"Device {device.device_id} connected to the network")

    def sendTask(self, device: Device, task: Task):
        if device.available:
            return device.execute(task)
        return None

    def receiveResult(self, task: Task):
        return task.result
