
#read the input 
n = int(input())

count = 0
# n the iteration of the for loop 
for _  in range(n):
    
    # Read the views person 
    views = list(map(int,input().split()))

    # sure of the problem sulation 
    sure_view = sum(views)

    # if the two sulation of the problem count the views  increament the value 

    if sure_view >= 2:
        count += 1
    
print(count)

