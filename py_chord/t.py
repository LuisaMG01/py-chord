import grpc
import chord_pb2
import chord_pb2_grpc
from .abc import IChordNetwork, INode
from typing import List

CHORD_PORT = 6666
MAINTENANCE_FREQUENCY = 60  # seconds

class Finger:
    def __init__(self):
        self.start: int = 0
        self.node: INode = None

class ChordNetwork(IChordNetwork):
    def __init__(self, node: INode):
        self.node = node
        self.finger_table: List[Finger] = [Finger() for _ in range(160)]  # Assuming 160-bit SHA-1
        self._init_finger_table()

    def _init_finger_table(self):
        for i in range(160):
            self.finger_table[i].start = (self.node.id + 2**i) % (2**160)

    async def join(self, node: INode = None):
        if node:
            async with grpc.aio.insecure_channel(f'{node.ip}:{node.port}') as channel:
                stub = chord_pb2_grpc.ChordServiceStub(channel)
                await self._init_finger_table(stub)
                await self._update_others(stub)
        else:
            for finger in self.finger_table:
                finger.node = self.node
            self.node._predecessor = self.node

    async def mantain(self):
        await self.stabilize()
        await self.fix_fingers()
        # Implement other maintenance tasks

    async def stabilize(self):
        successor = await self.node._get_successor()
        async with grpc.aio.insecure_channel(f'{successor.ip}:{successor.port}') as channel:
            stub = chord_pb2_grpc.ChordServiceStub(channel)
            predecessor_response = await stub.GetPredecessor(chord_pb2.Empty())
            predecessor = INode(predecessor_response.ip, predecessor_response.port)
            if is_between(predecessor.id, self.node.id, successor.id):
                await self.node._set_successor(predecessor)
            await stub.Notify(chord_pb2.Node(ip=self.node.ip, port=self.node.port, id=self.node.id))

    async def fix_fingers(self):
        for i in range(1, 160):
            successor = await self.node._find_successor(self.finger_table[i].start)
            self.finger_table[i].node = successor

    def remove_left_node(self, node: INode):
        for finger in self.finger_table:
            if finger.node == node:
                finger.node = None

    async def _init_finger_table(self, stub: chord_pb2_grpc.ChordServiceStub):
        successor_response = await stub.FindSuccessor(chord_pb2.IdRequest(id=self.finger_table[0].start))
        self.finger_table[0].node = INode(successor_response.ip, successor_response.port)
        predecessor_response = await stub.GetPredecessor(chord_pb2.Empty())
        self.node._predecessor = INode(predecessor_response.ip, predecessor_response.port)
        await stub.SetPredecessor(chord_pb2.Node(ip=self.node.ip, port=self.node.port, id=self.node.id))
        
        for i in range(159):
            if is_between(self.finger_table[i+1].start, self.node.id, self.finger_table[i].node.id):
                self.finger_table[i+1].node = self.finger_table[i].node
            else:
                finger_response = await stub.FindSuccessor(chord_pb2.IdRequest(id=self.finger_table[i+1].start))
                self.finger_table[i+1].node = INode(finger_response.ip, finger_response.port)

    async def _update_others(self, stub: chord_pb2_grpc.ChordServiceStub):
        for i in range(160):
            predecessor_id = (self.node.id - 2**i) % (2**160)
            predecessor_response = await self._find_predecessor(predecessor_id)
            async with grpc.aio.insecure_channel(f'{predecessor_response.ip}:{predecessor_response.port}') as channel:
                pred_stub = chord_pb2_grpc.ChordServiceStub(channel)
                await pred_stub.UpdateFingerTable(chord_pb2.UpdateFingerTableRequest(
                    node=chord_pb2.Node(ip=self.node.ip, port=self.node.port, id=self.node.id),
                    index=i
                ))

    async def _find_predecessor(self, id: int) -> INode:
        node = self.node
        while not is_between(id, node.id, await node._get_successor().id, right_inclusive=True):
            node = await node._closest_preceding_finger(id)
        return node

def is_between(id: int, start: int, end: int, right_inclusive: bool = False) -> bool:
    if start < end:
        return start < id < end or (right_inclusive and id == end)
    return start < id or id < end or (right_inclusive and id == end)