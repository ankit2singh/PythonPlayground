# def addd(a,b):
#      return a+b 
# print("Hello")
# if __name__ == "__main__":
#   addd(9,7)  
#   print("bye")

class Solution:
    def reverse(self, x: int) -> int:
        revint = 0
        while(x>0):
            revint=revint*10 + x%10
            x //=10
        return revint

ob = Solution()
print(ob.reverse(123))        