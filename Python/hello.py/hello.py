import random


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.data = set()

    def gossip(self, nodes):
        if not nodes:
            return

        target = random.choice(nodes)

        # merge knowledge
        combined = self.data.union(target.data)

        self.data = combined
        target.data = combined


def run_gossip(nodes, rounds=5):
    for _ in range(rounds):
        for node in nodes:
            other_nodes = [n for n in nodes if n != node]
            node.gossip(other_nodes)

    return [node.data for node in nodes]