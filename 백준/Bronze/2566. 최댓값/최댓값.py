M = []
MAX = 0
for row in range(9):
    row = list(map(int, input().split()))
    M.append(row)
MAX = max(map(max, M))
index = [(i+1,j+1) for i in range(9) for j in range(9) if M[i][j] == MAX]
print(MAX)
print(*index[0])