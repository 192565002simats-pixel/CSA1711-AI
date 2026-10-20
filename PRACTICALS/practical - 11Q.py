colors = ['Red', 'Green', 'Blue']

n = int(input("Enter number of regions: "))
graph = {}

for i in range(n):
    region = input("Enter region name: ")
    neighbors = input("Enter neighboring regions separated by space: ").split()
    graph[region] = neighbors

color = {}

def solve(node):
    if node == len(graph):
        return True

    region = list(graph.keys())[node]

    for c in colors:
        if all(color.get(neighbor) != c for neighbor in graph[region]):
            color[region] = c

            if solve(node + 1):
                return True

            del color[region]

    return False

if solve(0):
    print("\nMap Coloring Solution:")
    for region in color:
        print(region, ":", color[region])
else:
    print("No solution exists")
