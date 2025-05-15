n=int(input())
all_info=[]

for i in range(n):
    inform=input().split()
    all_info.append(inform)

sorted_info=sorted(all_info,key=lambda x:int(x[0]))

for info in sorted_info:
    print(' '.join(info))