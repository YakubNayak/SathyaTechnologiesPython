s="Learning Python is very Easy"
n=len(s)
i=0
print("Forword Direction")
while i<n:
    print(s[i],end="")
    i=i+1
print()
print("Backword Direction")
i=-1
while i>=-n:
    print(s[i],end="")
    i=i-1
