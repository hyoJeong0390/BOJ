word = input()
li = []
for i in range(26):
    li.append(-1)

for i in range(len(word)):
    c = ord(word[i])
    if li[c-97] == -1:
        li[c-97] = i

for j in range(len(li)):
    print(li[j], end=' ')
    
    
#2
print(*map(input().find,map(chr,range(97,123))))
