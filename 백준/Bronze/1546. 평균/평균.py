n = int(input())
score = list(map(int,input().split()))
MAX = max(score)
sum = 0
for i in range(len(score)):
    sum += score[i]/MAX*100
print(sum/n)