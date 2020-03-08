memo = {}
def denomination(coin):
    if coin <=2:
        return coin
    if coin in memo:
        return memo[coin]
    else:
        memo[coin] = max(coin, denomination(coin//2)+denomination(coin//3)+denomination(coin//4))
    return memo[coin]
for _ in range(10):
    try:
        coin = int(input())
        print(denomination(coin))
    except:
        break
