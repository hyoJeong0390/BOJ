word = str(input())
time = 0

for i in word:
    if ord(i) < 68:
        dial = 2
    elif ord(i) < 71:
        dial = 3
    elif ord(i) < 74:
        dial = 4
    elif ord(i) < 77:
        dial = 5
    elif ord(i) < 80:
        dial = 6
    elif ord(i) < 84:
        dial = 7
    elif ord(i) < 87:
        dial = 8
    else:
        dial = 9
    time += dial + 1

print(time)
