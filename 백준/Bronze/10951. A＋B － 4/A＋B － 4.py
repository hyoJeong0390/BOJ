# 이 문제는 테스트를 중단하는 조건이 별도로 없기 때문에 입력 형식에 벗어날 경우 while문을 종료하도록 코드를 작성
while True:
    try:
        A, B = map(int, input().split())
        print(A + B)
    except:
        break
