import asyncio
import random
from node import Node
from network import ChordNetwork, CHORD_PORT

async def create_node(ip, port):
    node = Node(ip, port)
    await node.start_grpc_server()
    return node

async def join_network(node, existing_node=None):
    if existing_node:
        await node.network.join(existing_node)
    else:
        await node.network.join()

async def test_store_and_get(nodes, num_operations=10):
    for _ in range(num_operations):
        storing_node = random.choice(nodes)
        value = f"test_value_{random.randint(1, 1000)}".encode()
        key = await storing_node.store(value)
        print(f"Stored value with key: {key}")

        retrieving_node = random.choice(nodes)
        retrieved_value = await retrieving_node.get(key)
        print(f"Retrieved value: {retrieved_value.decode()}")

        assert value == retrieved_value, "Stored and retrieved values don't match"

async def main():
    num_nodes = 5
    nodes = []

    # Create and start nodes
    for i in range(num_nodes):
        node = await create_node("127.0.0.1", CHORD_PORT + i)
        nodes.append(node)

    # Join nodes to the network
    await join_network(nodes[0])  # First node creates the network
    for node in nodes[1:]:
        await join_network(node, nodes[0])  # Other nodes join through the first node

    # Wait for the network to stabilize
    await asyncio.sleep(5)

    # Test storing and retrieving data
    await test_store_and_get(nodes)

    # Stop all nodes
    for node in nodes:
        await node.stop_grpc_server()

if __name__ == "__main__":
    asyncio.run(main())