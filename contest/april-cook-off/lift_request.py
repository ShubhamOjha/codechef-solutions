T = int(input())
for _ in range(T):
    N, Q = list(map(int, input().split()))
    present_floor = 0
    floor_cost = 0
    for _ in range(int(Q)):
        f, d = list(map(int, input().split()))
        floor_cost += abs(present_floor - f)
        present_floor = f
        floor_cost += abs(present_floor - d)
        present_floor = d
    print(floor_cost)