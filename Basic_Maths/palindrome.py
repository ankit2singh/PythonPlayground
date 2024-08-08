class Solution:
    def isPalindrome(self, x: int) -> bool:
           y =str(x)
           rev = y[::-1]
           if rev == y:
            return True
           else:
            return False

ob = Solution()         
print(ob.isPalindrome(323231)) 
  