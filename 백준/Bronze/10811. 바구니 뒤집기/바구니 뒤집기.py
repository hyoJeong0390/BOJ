n, m = map(int, input().split())
b = [i+1 for i in range(n)]
for k in range(m):
    i, j = map(int, input().split())
    b_tmp = b[i-1:j]
    b_tmp.reverse()
    for l in range(j-i+1):
        b[i-1] = b_tmp[l]
        i += 1
print(*b)