# t = int(input())


# sum = 0
# for i in range(t):
#     y = int(input())
#     for x in range(3,y):
#             # if   (x  %  3== 0  or  x %  5 == 0 ) :
#             #         if (x % 3 == 0 and x % 5 == 0) :
#             #             continue
#             #         else:
#             #             sum += x
#             #             print(x)

#             if x % 3 == 0 or x %  5 == 0 and x % 5  != 0:
#                     sum += x
                  
# print(sum)


# # # lst = []
# # # for i in range(1,t+1):
# # #     n = int(input())
# # #     lst.append(n)
# # # for i in lst:
# # #     print(i,end=" ")



# # def multiples_values_sum(a,b):
# #     res = a  + b
# #     print(res)


# # t = int(input("Enter Your TestCase Input  ; "))

# # for i in range(1,t):


t = int(input())


sum = 0
for i in range(t):
    y = int(input())
    for x in range(3,y):
            if  x  %  3  == 0  or  x %  5 == 0  and   x % 3 != 0:
                    sum += x
                    # print(x)
    print(sum)



