N = int(input("Enter integer: "))
R = 1
D = 1
forever = 1
while forever == 1:
    print(R)
    if R**3 > N:
        R = R-D
        if D <= 0.01:
            forever = forever+2
        else:
         D = D/10
    else:
       R = R+D

print("The cube root of "+str(N)+" is approximately "+str(R))
