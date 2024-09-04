def highestlowest(arr):
    mpp={}
    for i in arr:
       if i in mpp:
           mpp[i] +=1
       else:
           mpp[i] = 1  
    low=1000
    high=0
    for k in mpp:
        if mpp[k]>high:
            high = mpp[k]     
        if mpp[k]<low:
            low = mpp[k]
        
    return mpp,high,low
      
          

print(highestlowest([1,1,12,5,3,4,4,4]))        

