n = int(input())


count = 0

for _ in range(n):

    statement = input()

    if "++" in statement:
      count +=1
    else:
     count -=1


print(count)