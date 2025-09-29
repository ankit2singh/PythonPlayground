def getSecondOrderElements(a):
    

    largest= float("-inf")
    s_largest= float("-inf")

    for i in range(0, len(a)):

        if a[i] > largest:

            s_largest = largest

            largest = a[i]
        
        if a[i] > s_largest and a[i] != largest:
            s_largest = a[i]
                 
    return [s_largest]    
   
print(getSecondOrderElements([3,4,5,6,6]))
