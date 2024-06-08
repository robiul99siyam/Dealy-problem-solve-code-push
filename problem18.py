def encoding_dns (N,S):
    encode = ''
    for i in range(0,N,2):

        if S[i:i+2] == "00":
            encode += "A"
        elif S[i:i+2] == "11":
            encode += "G"
        elif S[i:i+2] == "10":
            encode += "C"
        elif S[i:i+2] == "01":
            encode += "T"
    return encode
   



T  = int(input())

for _ in range(T):
    n = int(input())
    s = input().strip()
    print(encoding_dns(n,s))