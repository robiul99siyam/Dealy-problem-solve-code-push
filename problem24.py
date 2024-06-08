# white a function 
def string_gectornetor(n):
    if n == 0:
        print("YES\n")
    if n == 1 and t == 1:
        print("NO\n")
    s = ""
    for _ in range(n):
        if not s or s[-1] == 'A':
            s+="B"
        else:
            s+="A"
    return "YES\n" + s
    

t = int(input())

for _ in range(t):
    n = int(input())
    print(string_gectornetor(n))
