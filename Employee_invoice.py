empid=int(input("enter Your Employee Id:"))
empname=input("enter Your Employee name:")
emp_bsal=float(input("enter Your Employee basic salary:"))
print("Employee Id=",empid)
print("Employee Name=",empname)
print("Employee Basic Salary=",emp_bsal)
if emp_bsal>0 and emp_bsal<20000:
    ta=(emp_bsal*7.75)/100
    da=(emp_bsal*8.75)/100
    hra=(emp_bsal*11.25)/100
    pf=(emp_bsal*12.25)/100
    lic=(emp_bsal*5.75)/100
    print("TA={},DA={},HRA={}".format(ta,da,hra))
    print("PF={},LIC={}".format(pf,lic))
    grass_salary=emp_bsal+ta+da+hra
    net_sal=grass_salary-(pf+lic)
    print("Grass salary=",  grass_salary)
    print("Nesalary =",net_sal)

elif emp_bsal>=20000 and emp_bsal<40000:
    ta=(emp_bsal*11.75)/100
    da=(emp_bsal*18.75)/100
    hra=(emp_bsal*11.25)/100
    pf=(emp_bsal*16.25)/100
    lic=(emp_bsal*55.75)/100
    print("TA={},DA={},HRA={}".format(ta,da,hra))
    print("PF={},LIC={}".format(pf,lic))
    grass_salary=emp_bsal+ta+da+hra
    net_sal=grass_salary-(pf+lic)
    print("Grass salary=",  grass_salary)
    print("Nesalary =",net_sal)
elif emp_bsal>=40000:
    ta=(emp_bsal*27.75)/100
    da=(emp_bsal*18.75)/100
    hra=(emp_bsal*14.25)/100
    pf=(emp_bsal*12.25)/100
    lic=(emp_bsal*25.75)/100
    print("TA={},DA={},HRA={}".format(ta,da,hra))
    print("PF={},LIC={}".format(pf,lic))
    grass_salary=emp_bsal+ta+da+hra
    net_sal=grass_salary-(pf+lic)
    print("Grass salary=",  grass_salary)
    print("Nesalary =",net_sal)
else:
    print("Invalid Data")
print("Thanks")
