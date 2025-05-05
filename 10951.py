while True:
    try: # 정상 입력이 들어왔을 때 실행할 블록
        a,b=map(int,input().split())
        print(a+b)
    except EOFError: # 비정상 입력 -> 입력x 탈출
        break
