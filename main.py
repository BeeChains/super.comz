from supercomputer import SuperComputer
from device import Device
from task import Task

if __name__ == "__main__":
    super_computer = SuperComputer()

    # Adding devices
    device1 = Device("Device1")
    device2 = Device("Device2")
    super_computer.addDevice(device1)
    super_computer.addDevice(device2)

    # Creating and distributing tasks
    task1 = Task("Task1", "Process Data 1")
    task2 = Task("Task2", "Process Data 2")

    super_computer.distributeTask(task1)
    super_computer.distributeTask(task2)

    # Collecting results
    results = super_computer.collectResults()
    print("Collected results:", results)
