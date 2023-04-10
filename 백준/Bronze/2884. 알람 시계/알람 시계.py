H, M = map(int, input().split())
al_M = M - 45
if al_M < 0:
    if H == 0:
        H = 24
    al_M += 60
    al_H = H - 1
    print(al_H, al_M)
else:
    print(H, al_M)