import sys

sys.setrecursionlimit(10**8)


def dfs(G, v, p, d, depth, subtree_size):
    depth[v] = d
    for nv in G[v]:
        if nv == p:
            continue
        dfs(G, nv, v, d + 1, depth, subtree_size)

    subtree_size[v] = 1
    for c in G[v]:
        if c == p:
            continue
        subtree_size[v] += subtree_size[c]


def main():
    N = int(input())

    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)

    root = 0
    depth = [0] * N
    subtree_size = [0] * N
    dfs(G, root, -1, 0, depth, subtree_size)

    ans = 10**8
    for v in range(N):
        if depth[v] == 1:
            ans = min(N - subtree_size[v], ans)

    print(ans)


if __name__ == "__main__":
    main()
