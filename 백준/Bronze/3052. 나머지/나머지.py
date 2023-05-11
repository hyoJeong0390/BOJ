remain = []
cnt = 10
for i in range(10):
    num = int(input())
    remain.append(num % 42)
    if (num % 42) in remain[:-1] :
        cnt -= 1
    else:
        continue
print(cnt)
        