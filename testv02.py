min =11110
arr = [11,34,3,2,6,4]
for j in range(len(arr)):
    if min > arr[j]:
      min = arr[j]
    j +=1 

print(min)    