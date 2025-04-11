from abc import ABC, abstractmethod
from src.resource import Resource
from typing import List

class Executable(ABC):
    def __init__(self, name:str,
                 description: str,
                 required_resources_names: List[str],
                 duration_in_units: int):
        if not name:
            raise ValueError("Executable name cannot be empty")
        if duration_in_units <= 0:
            raise ValueError(f"Duration in units for {name} must be positive")
        self._name = name
        self._description = description
        self._required_resources_names = required_resources_names
        self._duration_in_units = duration_in_units
        self._assigned_resources: List[Resource] = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def required_resources_names(self) -> List[str]:
        return self._required_resources_names

    @property
    def duration_in_units(self) -> int:
        return self._duration_in_units

    def assign_resources(self, resource_pool: List[Resource]) -> None:
        self._assigned_resources.clear()
        if not self._required_resources_names:
            return

        for resource_name in self._required_resources_names:
            found = False
            for resource in resource_pool:
                if resource.name == resource_name and resource.is_available_for_use():
                    resource.allocate()
                    self._assigned_resources.append(resource)
                    found = True
                    break
            if not found:
                self.release_resources()
                raise RuntimeError(f"Resource '{resource_name}' not available")


    def release_resources(self) -> None:
        for resource in self._assigned_resources:
            try:
                resource.release()
            except Exception as e:
                print(f"Failed to release '{resource.name}' in '{self.name}': {e}")
        self._assigned_resources.clear()

    @abstractmethod
    def execute(self) -> None:
        pass

    def can_execute(self, resource_pool: List[Resource]) -> bool:
        if not self._required_resources_names:
            return True
        for resource_name in self._required_resources_names:
            if not any(r.name == resource_name and r.is_available_for_use() for r in resource_pool):
                return False
        return True
