a = int(input())
b = int(input())
tmp1 = a * (b % 100 % 10)
tmp2 = a * ((b // 10) % 10)
tmp3 = a * (b // 100)
print(tmp1)
print(tmp2)
print(tmp3)
print((tmp1) + (tmp2*10) + (tmp3*100))