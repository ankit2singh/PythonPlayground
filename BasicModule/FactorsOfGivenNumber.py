def FON(n):

    res = []

    for i in range(1,(n//2)+1):
        if n%i == 0:
            res.append(i)
    res.append(n)
    return res        


print(FON(14))
######### Approach 2 most optimized #########
from math import sqrt

def FON2(n):

    res = []

    for i in range(1,int(sqrt(n))+1):
        if n%i == 0:
            res.append(i)
            if n//i != n:
                res.append(n//i)    
    res.append(n)
    return res      

print("FON2 ", FON2(14))