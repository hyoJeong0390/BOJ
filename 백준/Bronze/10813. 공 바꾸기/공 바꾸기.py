n, m = map(int, input().split())
basket = []
for i in range(n):
    basket.append(int(i+1))  // basket = [*range(1,N+1)]
for i in range(m):
    i, j = map(int, input().split())
    tmp = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = tmp  // basket[i-1],basket[j-1] = basket[j-1],basket[i-1]
print(*basket)
