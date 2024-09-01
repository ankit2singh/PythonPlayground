# ord('é')  # Returns 233, which is the Unicode code point for 'é'
# ord('Ω')  # Returns 937, which is the Unicode code point for 'Ω'
# ord('A')  # Returns 65, which is the ASCII value for 'A'


arr = 'AABabcaabbdz'

hash = [0] * 256

# print(hash[arr[1]])
for i in range(len(arr)):
    # hash[ord(arr[i]) - ord('a')] += 1
     hash[ord(arr[i])] += 1
    # print(i,hash[i])

# for i,val in enumerate(hash):   // for integer
#     print(i,val)   

for i in range(len(hash)):
     if hash[i]>0:
          print(i,hash[i])