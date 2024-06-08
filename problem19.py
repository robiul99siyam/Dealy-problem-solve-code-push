lst = []

n = int(input())
for i in range(0,n):
    ele = int(input())
    lst.append(ele)

    if ele >= 2000:
        print("YES")
    else:
        print("NO")
