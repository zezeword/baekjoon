n=int(input()) #숫자의 개수 변수
total=0 #N개의 합 출력 변수

num=input()

for i in num[:n]:
    total+=int(i)
    
print(total)



#range(start, stop, step)
#start: 시작값
#stop: 끝나는 값 바로 앞까지
#step: 증가 또는 감소 폭

#기본은 end="\n"이 생략 되어 있는거임