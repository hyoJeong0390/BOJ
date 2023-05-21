word = input()
cnt = 0
for i in range(len(word)//2):
    if word[i] == word[-1-i]:
        i += 1
        cnt += 1
    else:
        break
if cnt < (len(word) // 2):
    print(0)
else:
    print(1)