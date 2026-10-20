def minimax(depth, node, is_max):
    if depth == 2:
        return tree[node]

    if is_max:
        return max(minimax(depth + 1, node * 2, False),
                   minimax(depth + 1, node * 2 + 1, False))
    else:
        return min(minimax(depth + 1, node * 2, True),
                   minimax(depth + 1, node * 2 + 1, True))

tree = list(map(int, input("Enter 4 leaf values: ").split()))

print("Best value:", minimax(0, 0, True))
