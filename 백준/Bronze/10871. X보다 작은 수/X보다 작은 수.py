N, X = map(int, input().split())
a = input().split()
for i in range(len(a)):
    if int(a[i]) < X:
        print(a[i], end=' ')