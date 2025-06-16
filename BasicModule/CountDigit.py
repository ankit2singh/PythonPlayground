from math import ceil, log10

def cnt(x):
    return int(log10(x)+1) # +1 because for 3 digit it gives 2.somehing so addding 1 and using 
    # return ceil(log10(x))

def cnt_while(x):
    cnt = 0
    while x > 0:
        cnt +=1
        x = x//10
print(cnt(777))
print(cnt(7770))


