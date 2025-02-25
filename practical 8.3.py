s=set()
p=["sd","ya","mi","rcb","csk"]
q=["ysdn"]
s.update(p,q)
s=list(s)
s[0]="ds"
s.pop(2)
s.pop(3)
s=set(s)
print(s)

