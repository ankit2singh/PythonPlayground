arr = [5,7,7,8,9,2,5]

hash = [0] * 12

print(hash[arr[1]])
for i in arr:
    hash[i] += 1
    # print(i,hash[i])

for i,val in enumerate(hash):
    print(i,val)   