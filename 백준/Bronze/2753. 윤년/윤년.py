yy = int(input())
if (yy % 4) == 0:
    if (yy % 100) != 0:
        print("1")
    elif (yy % 400) == 0:
        print("1")
    else:
        print("0")
else:
    print("0")