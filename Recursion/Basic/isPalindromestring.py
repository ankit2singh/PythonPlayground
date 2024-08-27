class Solution:
    def isPalindrome(self, s: str) -> bool:            
        s = [c.lower() for c in s if c.isalnum()]    # list comprehension syntax [expression for item in iterable if condition]
        return all (s[i] == s[~i] for i in range(len(s)//2))
    

ob = Solution()
print(ob.isPalindrome('abccba'))    