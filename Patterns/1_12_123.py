# 1 
# 1 2 
# 1 2 3
def pat(n):
    for i in range(n):        
     for j in range(i):      
        print((j+1), end=' ')
        j +=1
     print()
pat(5)        