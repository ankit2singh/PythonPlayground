# Input: n = 2446
# Output: 1
# Explanation: Here among 2, 4, 6 only 2 divides 2446 evenly while 4 and 6 do not.


class Solution:
    def evenlyDivides (self, N):
        k=N
        sol = 0
        while(N!= 0):
            digit = N % 10
            N = N//10
            if digit != 0 and k % digit == 0:
             sol += 1 #.append(digit)
             #print(sol)
            # else:
            #    return 0#print("try again")
        return sol       
        
ob = Solution()
print(ob.evenlyDivides(2446))        