import sys

sys.setrecursionlimit(10**8)

dist1_list = [set(["A", "B"]), set(["B", "C"]), set(["C", "D"]), set(["D", "E"]), set(["E", "A"])]

s = list(input())
t = list(input())

if (set(s) in dist1_list) and (set(t) in dist1_list):
    print("Yes")

elif (set(s) not in dist1_list) and (set(t) not in dist1_list):
    print("Yes")

else:
    print("No")
