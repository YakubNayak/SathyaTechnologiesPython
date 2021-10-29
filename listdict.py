countries=["usa","india","germany","france"]
cities=['washington','new delhi','berlin','paris']



#make a dictionary
z=zip(countries,cities)
print(z)
d=dict(z)  
print(d)
print('{:25s}---{:15s}:'.format('COUNTRY','CAPITAL'))
for k in d:
       
        print('{:25s}---{:15s}'.format(k,d[k]))

