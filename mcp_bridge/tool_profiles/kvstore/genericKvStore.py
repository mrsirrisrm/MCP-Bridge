from abc import ABC

class genericKvStore(ABC):
    """Generic key-value store"""
    prefix: str

    def __init__(self, prefix: str) -> None:
        """Initialize the store"""
        self.prefix = prefix

    @abstractmethod
    async def get(self, key: str) -> str:
        """Get a value from the store"""
        raise NotImplementedError("get not implemented")

    @abstractmethod
    async def set(self, key: str, value: str) -> None:
        """Set a value in the store"""
        raise NotImplementedError("set not implemented")
    
    @abstractmethod
    async def delete(self, key: str) -> None:
        """Delete a value from the store"""
        raise NotImplementedError("delete not implemented")
    
    @abstractmethod
    async def list_keys(self) -> list[str]:
        """List all keys in the store"""
        raise NotImplementedError("list_keys not implemented")