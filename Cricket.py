cricket={}
n=int(input("Enter number of players:"))
for values in range(n):
    print("Enter player name:",end=" ")
    k=input()
    print("Enter number of runs:",end=" " )
    v=int(input())
    cricket.update({k:v})
print(cricket)
# display all palyer names
print("Print Player Names")
for pname in cricket.keys():
    print(pname)
print("==========================")
# get Runs
print("enter palyer Name",end=" ")
name=input()

runs=cricket.get(name,-1)
if(runs==-1):
    print("No Player available")
else:
    print("Name={} Made a runs={}".format(name,runs))

    
    
    
