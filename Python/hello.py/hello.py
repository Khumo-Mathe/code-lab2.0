from heapq import heappush, heappop


def find_shortest_path(graph, start, end):
    """
    Uses Dijkstra's Algorithm to find the shortest path
    between two locations in a weighted graph.

    Args:
        graph (dict): Graph structure with weights
        start (str): Starting node
        end (str): Destination node

    Returns:
        dict: Shortest distance and path
    """

    priority_queue = []
    heappush(priority_queue, (0, start))

    distances = {
        node: float("inf")
        for node in graph
    }

    previous_nodes = {
        node: None
        for node in graph
    }

    distances[start] = 0

    while priority_queue:
        current_distance, current_node = heappop(priority_queue)

        # Skip outdated queue entries
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Found shorter path
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node

                heappush(
                    priority_queue,
                    (distance, neighbor)
                )

    # Reconstruct path
    path = []
    current = end

    while current:
        path.append(current)
        current = previous_nodes[current]

    path.reverse()

    return {
        "distance": distances[end],
        "path": path
    }


# Example weighted graph
city_map = {
    "A": {"B": 4, "C": 2},
    "B": {"A": 4, "D": 5},
    "C": {"A": 2, "D": 8, "E": 10},
    "D": {"B": 5, "C": 8, "E": 2},
    "E": {"C": 10, "D": 2}
}

result = find_shortest_path(
    city_map,
    start="A",
    end="E"
)