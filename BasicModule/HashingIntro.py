## Hashing can be done by 2 way, 1. Dictionary (common), 2. By List(if length is fixed like string or 1<n<20)
# TC -> O(n) + O(m)  SC -> O(1)

# for hash_list

s = 'abchfuyshkdxcdsxx'
q = ['a', 'f' ,'x'] # to find frequency

# we know that abc d is fixed length so we use list

hash_list = [0] * 26

for ch in s:
    ascii = ord(ch)
    idx = ascii - 97
    hash_list[idx] += 1
print("hash_list: ", hash_list)
for ch in q:
    idx = ord(ch) - 97
    print(hash_list[idx])

# for dict
hash_dict = {}
for i in s:
    hash_dict[i] = hash_dict.get(i,0) + 1
print(hash_dict)