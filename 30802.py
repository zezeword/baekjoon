N=int(input()) #S+M+L+XL+XXL+XXXL=N
sizes=list(map(int,input().split()))
#S,M,L,XL,XXL,XXXL=map(int,input().split()) 
T,P=map(int,input().split()) #Tshirt, pen

# pen : 23 = 7*3+2 딱 맞게 줘야함
# shirt : 더많게 줘도 ok

bundle_t=0
for people in sizes:
    bundle_t+=(people+T-1)//T 

#ceil 구현: 이미 나누어 떨어질 때는 +1하면 오버
# -> T-1로 처리

print(bundle_t)
bundle_pen=N//P
num_pen=N%P
print(bundle_pen,num_pen)

