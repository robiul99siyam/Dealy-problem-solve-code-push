n = int(input())

for i in range(0,n):
    a,b = map(int,input().split())

    if 6 < a+b:
        print("Yes")
    else:
        print("No")