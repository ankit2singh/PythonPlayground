def prime(n):
    for i in range(1,n):
        if n%i ==0:
            return True
        else:
            return False
        

def AllDivisor(n):
    res = []
    for i in range(1,n):
        if n%i ==0:  
            res.append(i)   
    return res           

print(prime(5))    
print(AllDivisor(36))    