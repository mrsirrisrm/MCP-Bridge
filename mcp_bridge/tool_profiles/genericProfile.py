from abc import ABC, abstractmethod
from typing import Literal
from mcp import ListToolsResult

from kvstore.genericKvStore import genericKvStore


class genericProfile(ABC):
    """Generic tool profile class"""

    type: Literal["blacklist", "whitelist"]
    """Type of profile"""
    name: str
    """Name of the profile"""
    kv_store: genericKvStore
    """Key-value store for the profile"""

    def __init__(self, name: str, kv_store: genericKvStore) -> None:
        """Initialize the profile"""
        self.name = name
        self.kv_store = kv_store

    @abstractmethod
    def is_tool_allowed(self, tool_name: str) -> bool:
        """Check if a tool is allowed"""
        raise NotImplementedError("is_tool_allowed not implemented")

    @abstractmethod
    def block_tool(self, tool_name: str) -> None:
        """Block a tool"""
        raise NotImplementedError("block_tool not implemented")

    @abstractmethod
    def unblock_tool(self, tool_name: str) -> None:
        """Unblock a tool"""
        raise NotImplementedError("unblock_tool not implemented")

    @abstractmethod
    def list_allowed_tools(self) -> ListToolsResult:
        """List allowed tools"""
        raise NotImplementedError("list_allowed_tools not implemented")
