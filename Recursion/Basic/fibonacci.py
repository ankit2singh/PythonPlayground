# Example 1:
# Input: N = 5
# Output: 0 1 1 2 3 5
# Explanation: 0 1 1 2 3 5 is the fibonacci series up to 5th term.(0 based indexing)

def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib

n = 5
print(f"The Fibonacci Series up to {n}th term:")
print(fibonacci(n))

# #leetcode

# class Solution:
#     def fib(self, n: int) -> int:
#          if n==0:
#             return 0
#          if n==1:
#             return 1
#          return self.fib(n-1) + self.fib(n-2)