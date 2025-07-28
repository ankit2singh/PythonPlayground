from itertools import product, permutations, combinations, accumulate, groupby, count, cycle, repeat

# PRODUCT
a = [1,2]
b = [5,6]

print(list(product(a,b))) 
# o/p = [(1, 5), (1, 6), (2, 5), (2, 6)]

# PERMUTATION(all) AND COMBINATION(distinct)

x = [2,3,1,4]  

print("Combinatioon result: ", list(combinations(x,3)),"\nPermutaion Result: ", list(permutations(x, 2)))
# Combinatioon result:  [(2, 3, 1), (2, 3, 4), (2, 1, 4), (3, 1, 4)] 
# Permutaion Result:  [(2, 3), (2, 1), (2, 4), (3, 2), (3, 1), (3, 4), (1, 2), (1, 3), (1, 4), (4, 2), (4, 3), (4, 1)]

# ** ACCUMULATE

v = [1,2,3,4,5]
print("After Accumulation(sum): ", list(accumulate(v))) #its incremental
# After Accumulation(sum):  [1, 3, 6, 10, 15]


# if we want to accumulate by multiply.divide or max
import operator
print("After Accumulation(multiply): ", list(accumulate(v, func=operator.mul)))
# After Accumulation(multiply):  [1, 2, 6, 24, 120]

maxx = [1,2,-2,-1,0,7]
print("After Accumulation(max only): ", list(accumulate(maxx, func=max)))
# After Accumulation(max only):  [1, 2, 2, 2, 2, 7]


# count, cycle, repeat

for i in count(10):
    print(i)

    if i == 22: #  it will continue from 10 to infinity, to break it we use this condition
        break

for i in repeat(2, 11): # it will print 2 x11 times
    print(i)


for i in cycle(a):
    print(i) # infinite loop 
    if i==1:
        break


# ** group by -> it just o/p in two forms (True..., false...)

a = [1,2,3,4,5,6,7,8,9]

print(list(groupby(a)))
# [(1, <itertools._grouper object at 0x755ddc800820>), (2, <itertools._grouper object at 0x755ddc8010f0>), (3, <itertools._grouper object at 0x755ddc8011b0>), (4, <itertools._grouper object at 0x755ddc801180>), (5, <itertools._grouper object at 0x755ddc801240>), (6, <itertools._grouper object at 0x755ddc8012d0>), (7, <itertools._grouper object at 0x755ddc801360>), (8, <itertools._grouper object at 0x755ddc8013f0>), (9, <itertools._grouper object at 0x755ddc8014e0>)]

grpObj = groupby(a, key= lambda x: x>3)

for key, val in grpObj:
    print(key, list(val))

# False [1, 2, 3]
# True [4, 5, 6, 7, 8, 9]    
