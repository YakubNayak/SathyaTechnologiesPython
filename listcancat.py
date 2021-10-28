
lst=[]
n=int(input("Enter number of elements:")) #5
for item in range(n):
    value=int(input("enter value:"))
    lst.append(value)
print(lst)
sum=0
for s in lst:
    sum+=s
print("sum of lst =",sum)
