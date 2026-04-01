import heapq

def a_star(graph, start, goal, heuristic):
    open_set = [(0, start)]
    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0

    came_from = {}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor, weight in graph[current].items():
            tentative_g = g_cost[current] + weight

            if tentative_g < g_cost[neighbor]:
                came_from[neighbor] = current
                g_cost[neighbor] = tentative_g

                f_cost = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_cost, neighbor))

    return []


def reconstruct_path(came_from, current):
    path = [current]

    while current in came_from:
        current = came_from[current]
        path.append(current)

    return path[::-1]