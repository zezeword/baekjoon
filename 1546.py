n=int(input()) #시험 본 과목의 개수
scores=list(map(int,input().split())) #시험 성적
max=0
sum=0

for i in range(n):
    if max<scores[i]:
        max=scores[i]

for i in range(n):
    scores[i]=scores[i]/max*100
    sum+=scores[i]    

print(sum/n)

"""
py의list는 어떤 타입이든 담을 수 있음
list 자체는 가변이지만 그 안에 있는 int는 불변
리스트 안의 int 값은 바꿀 수 있지만
값 자체가 바뀌는것이 아니라 요소의 참조가 바뀌는 것
"""

