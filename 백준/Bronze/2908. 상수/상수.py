a, b = input().split()
li_a = list(a)
li_a.reverse()
a = int(''.join(li_a))
li_b = list(b)
li_b.reverse()
b = int(''.join(li_b))
print(max(a, b))