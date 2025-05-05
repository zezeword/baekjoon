n=int(input())
num=input()
a=list(map(int,num.split()))
print(min(a), max(a))

'''
1) input() -> 문자열 받기 ("10 20 30")
2) .split() -> 공백 기준으로 문자열을 나눠줌 ["10", "20", "30"]
3) map(int,...) -> 정수 리스트로 변환 [10, 20, 30]
4) list(...) -> 리스트로 감싸서 변수 a에 저장

'''
#map(함수, 반복가능한값)
#어떤 함수를 여러 값에 적용해서 새 값을 만드는 것
