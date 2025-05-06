re=int(input())
for i in range(re):
    n,text=map(str,input().split())
    n=int(n)
    p=""
    for i in text:
        p+=i*n
    print(p)
    

#print(출력내용,end="원하는문자")