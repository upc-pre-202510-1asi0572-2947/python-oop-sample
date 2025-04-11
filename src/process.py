from src.executable import Executable
from src.resource import Resource
from typing import List

class Process(Executable):
    def __init__(self,
                 name: str,
                 description: str,
                 required_resources_names: List[str],
                 duration_in_units: int):
        super().__init__(name, description, required_resources_names, duration_in_units)
        self._resource_pool: List[Resource] = []
        self._tasks: List[Executable] = []

    def add_resource(self, resource: Resource)->None:
        self._resource_pool.append(resource)

    def add_task(self, task: Executable)->None:
        self._tasks.append(task)

    def execute(self) -> None:
        if self._required_resources_names and len(self._assigned_resources) != len(self._required_resources_names):
            raise RuntimeError(f"Resources not properly assigned for process '{self.name}'")
        print(f"Executing process '{self.name}': {self._description} (Duration: {self._duration_in_units} units)")
        if self._assigned_resources:
            for resource in self._assigned_resources:
                resource.use()
        for task in self._tasks:
            try:
                if task.can_execute(self._resource_pool):
                    task.assign_resources(self._resource_pool)
                    print("  ", end="")
                    task.execute()
                    task.release_resources()
                else:
                    print(f"   Task '{task.name}' skipped: insufficient resources")
            except Exception as e:
                print(f"   Task '{task.name}' failed: {e}")

    def run(self)->None:
        try:
            if not self._required_resources_names or self.can_execute(self._resource_pool):
                if self._required_resources_names:
                    self.assign_resources(self._resource_pool)
                self.execute()
                self.release_resources()
                print(f"Process '{self.name}' completed successfully.")
            else:
                raise RuntimeError(f"Resources not properly assigned for process '{self.name}'")
        except Exception as e:
            print(f"   Process '{self.name}' failed: {e}")