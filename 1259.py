while True:
    num=input() # 숫자를 문자열로 받기
    if num=="0":
        break
    if num == num[::-1]: 
    # [start:stop:step] start,stop 생략 -> 처음부터 끝까지
    # step= -1 -> 몇 칸씩 이동할지(음수:역방향향)
        print("yes")
    else:
        print("no")
