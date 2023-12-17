import sys

sys.setrecursionlimit(10**8)

n = int(input())

rep = []
for i in range(12):
    rep.append(int("1" * (i + 1)))

ans_l = []
for j in rep:
    for k in rep:
        for m in rep:
            ans_l.append(j + k + m)


ans = list(set(ans_l))
ans.sort()

print(ans[n - 1])
