# hash table using map/dictionary
arr = [3,3,4,2,1,6,6]
mpp = {}

for i in range(len(arr)):
    if arr[i] in mpp:
        mpp[arr[i]] += 1
    else:
        mpp[arr[i]] = 1

print(mpp)        

