N = 3
for i in range(1,N+1):
    print('M',list(range(1,i-1)),N-i+1)
    print('M',i,list(range(N-i+1,N)))