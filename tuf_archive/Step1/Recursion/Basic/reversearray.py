
#Approach 1 with having extra space complexity
def revarr(n):
    k = []
    for i in range(len(n)-1,-1,-1):
        k.append(n[i])
    return k 

#print(revarr([3,4,5]))
   
# Approch 2: SLICING technique
# def revarr(n):
#     return n[::-1]
# print(revarr([3, 4, 5]))  # Output: [5, 4, 3]


#Approach 3: recursion
def revarr3(n,p1,p2):   
    if(p1<p2):
        n[p1],n[p2] = n[p2],n[p1]
        revarr3(n,p1+1,p2-1)

    return n    
print(revarr3([3,2,1],0,2))    

