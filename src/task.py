from src.executable import Executable

class Task(Executable):
    def __init__(self,
                 name: str,
                 description: str,
                 required_resources_names: list[str],
                 duration_in_units: int):
        super().__init__(name, description, required_resources_names, duration_in_units)

    def execute(self) -> None:
        if len(self._assigned_resources) != len(self.required_resources_names):
            raise RuntimeError(f"Resources not properly assigned to task '{self.name}'")
        print(f"Executing task '{self.name}': {self._description} (Duration: {self.duration_in_units} units)")
        for resource in self._assigned_resources:
            resource.use()
