def next_char_show (char):
    if char == "z":
        return "a"
    else:
        return chr(ord(char) + 1)

a = input()
res = next_char_show(a)
print(res)