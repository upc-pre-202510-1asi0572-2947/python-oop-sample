from abc import ABC, abstractmethod
from enum import Enum


class ResourceType(Enum):
    CONSUMABLE = "Consumable"
    USABLE = "Usable"


class Resource(ABC):
    def __init__(self, name: str, resource_type: ResourceType):
        self._name = name
        self._resource_type = resource_type
        self._is_available = True

    @property
    def name(self) -> str:
        return self._name

    @property
    def resource_type(self) -> ResourceType:
        return self._resource_type

    @abstractmethod
    def is_available_for_use(self) -> bool:
        """ Check if the resource is available for allocation.

        Returns:
            True if the resource is available for allocation, False otherwise.
        """
        pass

    @abstractmethod
    def allocate(self) -> None:
        pass

    @abstractmethod
    def release(self) -> None:
        pass

    @abstractmethod
    def use(self) -> None:
        pass
