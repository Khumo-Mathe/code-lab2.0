import random
import time


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.state = "FOLLOWER"
        self.votes = 0
        self.term = 0

    def start_election(self, nodes):
        self.state = "CANDIDATE"
        self.term += 1
        self.votes = 1  # vote for self

        for node in nodes:
            if node.node_id != self.node_id:
                if node.vote(self.term):
                    self.votes += 1

        if self.votes > len(nodes) // 2:
            self.state = "LEADER"
            return True

        self.state = "FOLLOWER"
        return False

    def vote(self, term):
        if term >= self.term:
            self.term = term
            return True
        return False