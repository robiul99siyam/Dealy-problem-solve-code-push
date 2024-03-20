lst = []

n = int(input())

for i in range(0,n):
    ele = int(input())
    lst.append(ele)
    if ele % 2 == 0:
        print("even")
    else:
        print("odd")
