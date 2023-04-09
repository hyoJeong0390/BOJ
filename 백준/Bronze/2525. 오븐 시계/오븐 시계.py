h, m = input().split()
h = int(h)
m = int(m)
need_t = int(input())
tmp = m + need_t
if tmp >= 60:
    h = h + tmp // 60
    if h >= 24:
        h = h % 24
print(h, tmp % 60)