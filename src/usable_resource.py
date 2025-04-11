from src.resource import Resource, ResourceType

class UsableResource(Resource):
    def __init__(self, name:str, capacity: int):
        super().__init__(name, ResourceType.USABLE)
        if capacity <= 0:
            raise ValueError(f"Capacity for resource '{self.name}' must be positive")
        self._capacity = capacity

    def is_available_for_use(self) -> bool:
        return self._is_available

    def allocate(self) -> None:
        if not self._is_available:
            raise RuntimeError(f"Usable resource '{self.name}' is already allocated")
        self._is_available = False

    def release(self) -> None:
        if self._is_available:
            print(f"Warning: Usable resource '{self.name}' is already released")
        self._is_available = True

    def use(self) -> None:
        print(f"Using Usable resource '{self.name}' (capacity: {self._capacity} GHz)")

