s = "D=M  //yeah"
for i in range(len(s)):
    if s[i] is '/' or s[i] is ' ':
        s = s[:i]
        break
print(len(s))
