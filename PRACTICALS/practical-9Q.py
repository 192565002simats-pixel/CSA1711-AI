
from itertools import permutations

n = int(input("Enter number of cities: "))

print("Enter cost matrix:")
cost = [list(map(int, input().split())) for _ in range(n)]

cities = list(range(1, n))
min_cost = float('inf')
best_path = []

for path in permutations(cities):
    route = (0,) + path + (0,)
    total = 0

    for i in range(n):
        total += cost[route[i]][route[i + 1]]

    if total < min_cost:
        min_cost = total
        best_path = route

print("Shortest path:", " -> ".join(str(c + 1) for c in best_path))
print("Minimum cost:", min_cost)

