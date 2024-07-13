class stack:
    
    def __init__(self):
        self.items = []
    

    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        
        
    def is_empty(self):
        return len(self.items)==0
    
    def display(self):
        print("stack of item display : ",self.items)


s = stack()
s.push(10)
s.push(20)
s.push(30)
# s.push(40)
# s.push(50)
s.pop()
s.display()





# n,m = map(int,input().split())
# p = '.|.'

# for i in range(n//2):
#     j = (i*2)+1
#     print((p * j).center(m,"-"))


# print("WELCOME".center(m,"-"))

# for i in reversed(range(n//2)):
#     j = (i*2)+1
#     print((p * j).center(m,"-"))




# def print_formated(number):
    
#     width = len(bin(n)[2:])
#     for i in range(1,n+1):


#         decimal = str(i)
#         octal = oct(i)[:2]
#         hexadeciaml = hex(i)[:2].upper()
#         binary = bin(i)[:2]

#         print(f"{decimal :>{width}} {octal :> {width}}")
        

    

# n = int(input())
# print_formated(n)



# def print_formet(size):
#     sent = string


# import string
# alpha = string.ascii_lowercase




# def print_rangoli(size):
#     lines = []
#     for row in range(size):
#         to_print = "-".join(alpha[row:size])
#         lines.append(to_print[::-1] + to_print[1:])
    
#     width = len(lines[0])
    

#     for row in range(size-1,0,-1):
#         print(lines[row].center(width,"-"))
    
#     for row in range(size):
#         print(lines[row].center(width,"-"))



n = print_rangoli(3)

