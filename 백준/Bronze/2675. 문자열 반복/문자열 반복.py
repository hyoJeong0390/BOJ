for i in range(int(input())):
    r, s = input().split()
    str = ''
    for j in range(len(s)):
        str += int(r) * s[j]
    print(str)