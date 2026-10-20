import math

def alphabeta(depth, node, alpha, beta, is_max):
    if depth == 2:
        return tree[node]

    if is_max:
        best = -math.inf
        for i in range(2):
            val = alphabeta(depth + 1, node * 2 + i,
                            alpha, beta, False)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = math.inf
        for i in range(2):
            val = alphabeta(depth + 1, node * 2 + i,
                            alpha, beta, True)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

tree = list(map(int, input("Enter 4 leaf values: ").split()))

print("Best value:", alphabeta(0, 0, -math.inf, math.inf, True))
