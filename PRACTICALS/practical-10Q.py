
def astar(graph, heuristic, start, goal):
    open_list = [(heuristic[start], start)]
    cost = {start: 0}
    path = {}

    while open_list:
        open_list.sort()
        _, node = open_list.pop(0)

        if node == goal:
            result = [node]
            while node in path:
                node = path[node]
                result.append(node)
            return result[::-1]

        for neighbor, distance in graph[node]:
            new_cost = cost[node] + distance

            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                path[neighbor] = node
                priority = new_cost + heuristic[neighbor]
                open_list.append((priority, neighbor))

    return None


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('E', 1)],
    'D': [('G', 5)],
    'E': [('G', 2)],
    'G': []
}

heuristic = {'A': 7, 'B': 6, 'C': 3, 'D': 4, 'E': 2, 'G': 0}

start = input("Enter start node: ").upper()
goal = input("Enter goal node: ").upper()

result = astar(graph, heuristic, start, goal)

if result:
    print("Path:", " -> ".join(result))
else:
    print("No path found")
