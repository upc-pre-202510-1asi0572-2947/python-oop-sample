from src.resource import Resource, ResourceType

class ConsumableResource(Resource):
    def __init__(self, name: str, capacity: int):
        super().__init__(name, ResourceType.CONSUMABLE)
        if capacity <= 0:
            raise ValueError(f"Capacity for resource '{name}' must be positive")
        self._total_capacity = capacity
        self._remaining_capacity = capacity

    def is_available_for_use(self) -> bool:
        return self._remaining_capacity > 0

    def allocate(self) -> None:
        if self._remaining_capacity <= 0:
            raise RuntimeError(f"No remaining capacity for resource '{self.name}'")
        self._remaining_capacity -= 1
        self._is_available = self._remaining_capacity > 0

    def release(self) -> None:
        if self._remaining_capacity == 0 and not not self._is_available:
            print(f"Warning: Consumable resource '{self.name}' can not be reused without replenishment")
        self._is_available = self._remaining_capacity > 0

    def use(self) -> None:
        print(f"  Using resource '{self.name}' (remaining:{self._remaining_capacity}/{self._total_capacity} MB)")

    @property
    def remaining_capacity(self) -> int:
        return self._remaining_capacity
