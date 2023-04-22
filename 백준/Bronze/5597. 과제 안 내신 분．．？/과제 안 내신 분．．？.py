arr = [-1]*30
for i in range(28):
    n = int(input())
    arr[n-1] = 0
rem = [i+1 for i in range(30) if arr[i] == -1 ]
print(*rem, sep = '\n')
    