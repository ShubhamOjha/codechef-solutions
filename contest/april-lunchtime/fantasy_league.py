t = int(input())
for _ in range(t):
    n, cost = list(map(int, input().split(' ')))
    costs = list(map(int, input().split(' ')))
    classification = list(map(int, input().split(' ')))
    def_for = {0:100,1:100}
    for i,value in enumerate(classification):
        if value == 0 and costs[i]<def_for[0]:
            def_for[0] = costs[i]
        elif value == 1 and costs[i]<def_for[1]:
            def_for[1] = costs[i]
    if sum(def_for.values())<=(100-cost):
        print('yes')
    else:
        print('no')

        