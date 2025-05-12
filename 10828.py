import sys

top = -1
stack=[]
stack_size=0

def empty():
    if top==-1:
        print("1")
    else:
        print("0")

def push(item):
    global top, stack_size #전역변수를 수정, 대입 할 경우 global 키워드 선언. 단, 읽기만 하는 경우는 필요없음
    stack.append(item)
    top+=1
    stack_size+=1

def pop():
    global top, stack_size
    if top==-1:
        print("-1")
    
    else:
        print(stack.pop())
        top-=1
        stack_size-=1

def peek():
    if top==-1:
        print("-1")
    
    else:
        print(stack[top])

def size():
    print(stack_size)


n=int(sys.stdin.readline())
for i in range(n):
    input_stack=sys.stdin.readline().strip()
    parts=input_stack.split()
    
    if parts[0] == "push":
        push(int(parts[1])) # 문자열을 숫자로 변환

    elif parts[0] == "pop":
        pop()

    elif parts[0] == "size":
        size()

    elif parts[0] == "empty":
        empty()

    elif parts[0] == "top":
        peek()

