t = int(input())
for _ in range(t):
    n = int(input())
    x = list(map(int, input().split(' ')))
    cluster_size = 1
    cluster = []
    for i in range(n-1):
        if (x[i+1] - x[i]) < 3:
            cluster_size +=1
        else:
            cluster.append(cluster_size)
            cluster_size = 1
    cluster.append(cluster_size)
    cluster.sort()
    print(cluster[0],cluster[-1])



