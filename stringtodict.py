#Converting a string into dictionary 
str="sai=10,pavan=20,priya=30,deeshitha=20,anusha=20,chandana=24"

lst=[]



for x in str.split(','):
	y=x.split('=')
	print(x)
	print(y)
	lst.append(y)
#convert the list into dictionary
d=dict(lst)
print(d)

# create the new dictionary 'd1' with name as string
d1={}
for k,v in d.items():
	d1[k]=v
print(d1)
