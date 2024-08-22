def fact(n):
    ans = 1
    i = 1
    while(i<=n):
        ans = ans*i
        i += 1
    return ans


print(fact(6))    



# # recursion
# def factorial_rec(n):
#     if n==0:
#         return factorial_rec(n)*factorial_rec(n-1)
    

# print(factorial_rec(6))    