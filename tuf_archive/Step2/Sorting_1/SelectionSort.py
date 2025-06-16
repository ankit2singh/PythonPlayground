def selctionsorts(arr):
      #arr = [11,34,3,2,6,4]      
      for i in range(len(arr)):
         min=i
         j=i+1
         for j in range(len(arr)):
           if arr[i] < arr[j]:
              min = j
           j +=1
           arr[min],arr[i]=arr[i],arr[min]  

      i += 1     
      return arr

print(selctionsorts(([11,34,3,2,6,4])))
    