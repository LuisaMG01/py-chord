from abc import abstractmethod, ABC
from hashlib import sha1
from typing import Any

ID_LENGTH = sha1().digest_size * 8

class IDHT(ABC):
    @abstractmethod
    async def store(self, value: bytes) -> int:
        pass

    @abstractmethod
    async def get(self, key: int) -> Any:
        pass

    @abstractmethod
    async def leave(self) -> None:
        pass

class INode(IDHT, ABC):
    def __init__(self, ip: str, port: int):
        self.ip = ip
        self.port = port
        hash = sha1()
        hash.update(ip.encode())
        hash.update(port.to_bytes(2, "big"))
        self.id = int.from_bytes(hash.digest(), "big")

    @abstractmethod
    async def start_grpc_server(self):
        pass

    @abstractmethod
    async def stop_grpc_server(self):
        pass

    @abstractmethod
    async def _is_alive(self):
        pass

    @abstractmethod
    async def _closest_preceding_finger(self, id: int) -> "INode":
        pass

    @abstractmethod
    async def _notify(self, node: "INode") -> None:
        pass

    @abstractmethod
    async def _get_successor(self) -> "INode":
        pass

    @abstractmethod
    async def _set_successor(self, node: "INode") -> None:
        pass

    @abstractmethod
    async def _get_predecessor(self) -> "INode":
        pass

    @abstractmethod
    async def _set_predecessor(self, node: "INode") -> None:
        pass

    @abstractmethod
    async def _find_successor(self, id: int) -> "INode":
        pass

    @abstractmethod
    async def _update_finger_table(self, node: "INode", index: int) -> None:
        pass

class IChordNetwork(ABC):
    @abstractmethod
    async def join(self, node: INode) -> None:
        pass

    @abstractmethod
    async def mantain(self) -> None:
        pass

    @abstractmethod
    async def stabilize(self):
        pass

    @abstractmethod
    async def fix_fingers(self):
        pass

    @abstractmethod
    def remove_left_node(self, node: INode):
        pass