piece = list(map(int, input().split()))
answer = [1, 1, 2, 2, 2, 8]
for i in range((len(piece))):
    piece[i] = answer[i] - piece[i]
print(*piece)