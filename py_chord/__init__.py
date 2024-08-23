from typing import Tuple
from .node import Node as _Node, RemoteNode as _RemoteNode
from .abc import INode

from .node import Node
from .network import ChordNetwork, CHORD_PORT


async def join_network(
    my_ip: str = "0.0.0.0", my_port: int = CHORD_PORT, bootstrap_node: Tuple = None
) -> INode:
    me = _Node(my_ip, my_port)
    await me._start_server()
    if bootstrap_node:
        entry_point = _RemoteNode(bootstrap_node[0], bootstrap_node[1])
    else:
        entry_point = None
    await me.network.join(entry_point)
    return me
