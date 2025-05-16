def prime(num):
    if num<=1:
        return 0
    else:
        for i in range(2,num):
            if num%i==0:
                return 0
    
    return 1

num=int(input()) #소수갯수
check_num=list(map(int,input().split()))

count=sum(prime(n) for n in check_num)
#sum()=0부터 시작해서 다 더한 결과
#제너레이터 표현식 (expression for item in iterable if 조건)
#ex1) (x * 2 for x in range(5)) -> 0, 2, 4, 6, 8
#ex2) sum(x for x in range(5)) ->0 + 1 + 2 + 3 + 4 → 10

'''
내가 처음 짠 코드
count=0
for i in range(num):
    if prime(check_num[i]):
        count+=1
'''
print(count)

